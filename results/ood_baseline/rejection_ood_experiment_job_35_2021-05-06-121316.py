store = {}
store['timestamp']=1620299596
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=35']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=35
store['worker_id']=35
store['num_workers']=40
store['config']={'seed': 50, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.14080810546875})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.355956554412842})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.795259475708008})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.943040132522583})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6872, 'crossentropy': 1.85677421875}
store['active_learning_steps'][0]['acquisition']={'indices': [36313, 17421, 12364, 50063, 34530], 'labels': [7, -1, 7, 1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.878933310508728})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.134765148162842})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.4413013458251953})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.435929775238037})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7311, 'crossentropy': 1.729323046875}
store['active_learning_steps'][1]['acquisition']={'indices': [47620, 51940, 46682, 4981, 14519], 'labels': [3, -1, -1, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.0738954544067383})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.5211589336395264})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.6390066146850586})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.6460838317871094})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7184, 'crossentropy': 1.833859375}
store['active_learning_steps'][2]['acquisition']={'indices': [1692, 22225, 6401, 30334, 33839], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.062133312225342})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.189655303955078})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.4998271465301514})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 2.424544334411621})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7417, 'crossentropy': 1.7368359375}
store['active_learning_steps'][3]['acquisition']={'indices': [10928, 7974, 5540, 24385, 35197], 'labels': [-1, -1, 7, 6, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.6926770210266113})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 2.1061453819274902})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 2.802889108657837})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 2.5609655380249023})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7698, 'crossentropy': 1.59132177734375}
store['active_learning_steps'][4]['acquisition']={'indices': [15839, 33124, 41537, 35000, 4363], 'labels': [-1, -1, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.7130635976791382})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 2.0242795944213867})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 2.101215362548828})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 2.225571393966675})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7491, 'crossentropy': 1.532541796875}
store['active_learning_steps'][5]['acquisition']={'indices': [14039, 36360, 57801, 28235, 17403], 'labels': [0, 9, 3, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.509150743484497})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.681776762008667})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.801125168800354})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.7689201831817627})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.766, 'crossentropy': 1.44480859375}
store['active_learning_steps'][6]['acquisition']={'indices': [25569, 44480, 26554, 14179, 13642], 'labels': [1, 5, 3, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.629536509513855})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.8373591899871826})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.8849804401397705})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.9710414409637451})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7641, 'crossentropy': 1.42616396484375}
store['active_learning_steps'][7]['acquisition']={'indices': [26005, 39115, 6996, 47409, 18035], 'labels': [9, 0, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.3901665210723877})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.7756527662277222})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.7431895732879639})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 2.0130906105041504})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7806, 'crossentropy': 1.20962509765625}
store['active_learning_steps'][8]['acquisition']={'indices': [21298, 55982, 59960, 8693, 2633], 'labels': [-1, -1, 5, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.4220914840698242})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.8619930744171143})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 2.0218565464019775})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.9478299617767334})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7933, 'crossentropy': 1.245401171875}
store['active_learning_steps'][9]['acquisition']={'indices': [13980, 15582, 4051, 34040, 35976], 'labels': [3, -1, -1, 8, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.3254077434539795})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.393024206161499})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.6588897705078125})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.5551602840423584})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7903, 'crossentropy': 1.21284951171875}
store['active_learning_steps'][10]['acquisition']={'indices': [20812, 49655, 32511, 49797, 35996], 'labels': [-1, -1, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.3493990898132324})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.6488059759140015})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.6634900569915771})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.9368906021118164})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7744, 'crossentropy': 1.1587404296875}
store['active_learning_steps'][11]['acquisition']={'indices': [36190, 47532, 28129, 20988, 39615], 'labels': [4, -1, -1, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.2864713668823242})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.3943270444869995})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.7904484272003174})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.7798932790756226})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7905, 'crossentropy': 1.15446533203125}
store['active_learning_steps'][12]['acquisition']={'indices': [19239, 58186, 13862, 19048, 52101], 'labels': [-1, -1, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.2283670902252197})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.5283703804016113})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.5346388816833496})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 2.001450538635254})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8047, 'crossentropy': 1.044025}
store['active_learning_steps'][13]['acquisition']={'indices': [24654, 59944, 2565, 24893, 8229], 'labels': [-1, -1, 2, 0, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.1625339984893799})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.3748152256011963})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.6422665119171143})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.7712039947509766})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7932, 'crossentropy': 1.08784287109375}
store['active_learning_steps'][14]['acquisition']={'indices': [56497, 52769, 16521, 46883, 3955], 'labels': [4, 5, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.341993808746338})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.5406010150909424})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.9606716632843018})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.9872480630874634})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.7872, 'crossentropy': 1.1914208984375}
store['active_learning_steps'][15]['acquisition']={'indices': [3623, 51826, 56303, 21162, 32662], 'labels': [-1, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.6213710308074951})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.59670090675354})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.746274471282959})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.9843215942382812})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.8633757829666138})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8052, 'crossentropy': 1.3307044921875}
store['active_learning_steps'][16]['acquisition']={'indices': [40513, 37456, 25150, 29383, 18116], 'labels': [-1, 8, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.310206651687622})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.6772873401641846})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.869657278060913})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.799844741821289})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.7945, 'crossentropy': 1.174246875}
store['active_learning_steps'][17]['acquisition']={'indices': [33265, 3221, 20684, 19511, 57179], 'labels': [-1, 6, -1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.333176612854004})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.4189393520355225})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.4324896335601807})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.6818132400512695})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8102, 'crossentropy': 1.1148646484375}
store['active_learning_steps'][18]['acquisition']={'indices': [33402, 43020, 15006, 43988, 57466], 'labels': [-1, -1, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.09598970413208})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.530922293663025})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.4855916500091553})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.5283267498016357})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8233, 'crossentropy': 1.004325}
store['active_learning_steps'][19]['acquisition']={'indices': [5130, 29518, 22245, 29821, 54624], 'labels': [9, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.3045156002044678})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.4895315170288086})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.5738887786865234})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.5509023666381836})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8124, 'crossentropy': 1.0616796875}
store['active_learning_steps'][20]['acquisition']={'indices': [21562, 31244, 22967, 2016, 6404], 'labels': [9, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.2675747871398926})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.350010871887207})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.4882744550704956})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.5857486724853516})
store['active_learning_steps'][21]['training']['best_epoch']=1
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8167, 'crossentropy': 1.0497580078125}
store['active_learning_steps'][21]['acquisition']={'indices': [15985, 37174, 358, 25188, 25083], 'labels': [-1, -1, 1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.246220588684082})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.5677299499511719})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.5449334383010864})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.5866726636886597})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8057, 'crossentropy': 1.1003072265625}
store['active_learning_steps'][22]['acquisition']={'indices': [22737, 19510, 19952, 38183, 51116], 'labels': [-1, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.1993913650512695})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.3350576162338257})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.4295647144317627})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.5775201320648193})
store['active_learning_steps'][23]['training']['best_epoch']=1
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.7972, 'crossentropy': 1.1119904296875}
store['active_learning_steps'][23]['acquisition']={'indices': [27457, 35130, 4303, 32170, 40904], 'labels': [1, -1, 7, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.247647762298584})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.4877359867095947})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.500356912612915})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.5757105350494385})
store['active_learning_steps'][24]['training']['best_epoch']=1
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.811, 'crossentropy': 1.08076845703125}
store['active_learning_steps'][24]['acquisition']={'indices': [28277, 40787, 22315, 43834, 28600], 'labels': [5, 8, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.1057655811309814})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.3011914491653442})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.5414423942565918})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.6390748023986816})
store['active_learning_steps'][25]['training']['best_epoch']=1
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8229, 'crossentropy': 1.0062953125}
store['active_learning_steps'][25]['acquisition']={'indices': [29460, 8941, 19057, 10416, 19199], 'labels': [-1, 3, 7, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.1366108655929565})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.2473303079605103})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.5262486934661865})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.587583303451538})
store['active_learning_steps'][26]['training']['best_epoch']=1
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8146, 'crossentropy': 1.01441435546875}
store['active_learning_steps'][26]['acquisition']={'indices': [49608, 25848, 11501, 53906, 46972], 'labels': [-1, -1, 0, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.1206395626068115})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.3301231861114502})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.456984281539917})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.53016996383667})
store['active_learning_steps'][27]['training']['best_epoch']=1
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8118, 'crossentropy': 1.026130859375}
store['active_learning_steps'][27]['acquisition']={'indices': [9061, 7625, 5261, 7871, 4117], 'labels': [9, 3, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.1358931064605713})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.3478822708129883})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.2372279167175293})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.3432352542877197})
store['active_learning_steps'][28]['training']['best_epoch']=1
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8196, 'crossentropy': 1.01577626953125}
store['active_learning_steps'][28]['acquisition']={'indices': [52355, 10647, 31261, 18178, 42766], 'labels': [9, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.137628197669983})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.1941494941711426})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.4571559429168701})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.7121427059173584})
store['active_learning_steps'][29]['training']['best_epoch']=1
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.7996, 'crossentropy': 1.08095283203125}
store['active_learning_steps'][29]['acquisition']={'indices': [25253, 42955, 10596, 5324, 36094], 'labels': [1, 5, 8, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.196303367614746})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.2257224321365356})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.2769145965576172})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.540380597114563})
store['active_learning_steps'][30]['training']['best_epoch']=1
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8078, 'crossentropy': 1.03159736328125}
store['active_learning_steps'][30]['acquisition']={'indices': [58279, 15321, 27482, 16636, 46785], 'labels': [-1, 8, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0581203699111938})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.1603199243545532})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.2758233547210693})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.2276432514190674})
store['active_learning_steps'][31]['training']['best_epoch']=1
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8221, 'crossentropy': 0.98051650390625}
store['active_learning_steps'][31]['acquisition']={'indices': [24770, 51309, 56289, 23292, 35927], 'labels': [3, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0507211685180664})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.205179214477539})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.5133378505706787})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.58918297290802})
store['active_learning_steps'][32]['training']['best_epoch']=1
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8045, 'crossentropy': 1.0444212890625}
store['active_learning_steps'][32]['acquisition']={'indices': [19718, 28586, 17589, 2578, 58822], 'labels': [9, 1, 6, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.113703727722168})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.0691863298416138})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.2734547853469849})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.3549535274505615})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.3950819969177246})
store['active_learning_steps'][33]['training']['best_epoch']=2
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8442, 'crossentropy': 0.9594849609375}
store['active_learning_steps'][33]['acquisition']={'indices': [34165, 37570, 59484, 44876, 51641], 'labels': [8, 2, 7, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9697079658508301})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.1832858324050903})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.1900060176849365})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.2670302391052246})
store['active_learning_steps'][34]['training']['best_epoch']=1
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8372, 'crossentropy': 0.90035751953125}
store['active_learning_steps'][34]['acquisition']={'indices': [38027, 37955, 34502, 38484, 16897], 'labels': [-1, 1, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0967819690704346})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.188295841217041})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.4117841720581055})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.460315465927124})
store['active_learning_steps'][35]['training']['best_epoch']=1
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8152, 'crossentropy': 1.014419140625}
store['active_learning_steps'][35]['acquisition']={'indices': [28231, 57897, 51700, 43094, 15799], 'labels': [5, -1, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.0077948570251465})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.105386734008789})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.2313940525054932})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.3416163921356201})
store['active_learning_steps'][36]['training']['best_epoch']=1
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8378, 'crossentropy': 0.9318}
store['active_learning_steps'][36]['acquisition']={'indices': [40132, 20685, 4130, 47726, 5616], 'labels': [-1, -1, 7, 8, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.0222337245941162})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.1826066970825195})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.3209196329116821})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.399212121963501})
store['active_learning_steps'][37]['training']['best_epoch']=1
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8005, 'crossentropy': 1.005934765625}
store['active_learning_steps'][37]['acquisition']={'indices': [14449, 12942, 12960, 10678, 25442], 'labels': [4, 3, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9347935318946838})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.0816736221313477})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.3444008827209473})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.2688415050506592})
store['active_learning_steps'][38]['training']['best_epoch']=1
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8201, 'crossentropy': 0.9324654296875}
store['active_learning_steps'][38]['acquisition']={'indices': [47239, 13790, 43566, 34440, 58847], 'labels': [6, -1, 2, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.95600426197052})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9433201551437378})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.1017791032791138})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.117835521697998})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.3011500835418701})
store['active_learning_steps'][39]['training']['best_epoch']=2
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8595, 'crossentropy': 0.91466220703125}
store['active_learning_steps'][39]['acquisition']={'indices': [10607, 56492, 38391, 15575, 19353], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9387289881706238})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.0822627544403076})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.2700111865997314})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.2279856204986572})
store['active_learning_steps'][40]['training']['best_epoch']=1
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8396, 'crossentropy': 0.875187890625}
store['active_learning_steps'][40]['acquisition']={'indices': [46964, 38104, 43099, 4513, 32148], 'labels': [-1, -1, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.0524276494979858})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.1442859172821045})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.1685341596603394})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.3076242208480835})
store['active_learning_steps'][41]['training']['best_epoch']=1
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8013, 'crossentropy': 1.01135986328125}
store['active_learning_steps'][41]['acquisition']={'indices': [2358, 12925, 50834, 17517, 34486], 'labels': [8, -1, 3, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9306951761245728})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.2062757015228271})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.2045841217041016})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.341649055480957})
store['active_learning_steps'][42]['training']['best_epoch']=1
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8291, 'crossentropy': 0.87036015625}
store['active_learning_steps'][42]['acquisition']={'indices': [27667, 56486, 59374, 57389, 24394], 'labels': [-1, 9, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.069501280784607})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.205232858657837})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.4282206296920776})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.493145227432251})
store['active_learning_steps'][43]['training']['best_epoch']=1
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.7962, 'crossentropy': 0.990409765625}
store['active_learning_steps'][43]['acquisition']={'indices': [17608, 3902, 50698, 28028, 50815], 'labels': [5, -1, 9, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9958527684211731})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0292739868164062})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1790094375610352})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.098940134048462})
store['active_learning_steps'][44]['training']['best_epoch']=1
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8135, 'crossentropy': 0.9874765625}
store['active_learning_steps'][44]['acquisition']={'indices': [57162, 23792, 36194, 23809, 34157], 'labels': [-1, -1, 9, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0010415315628052})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.1866625547409058})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.203345775604248})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.5116541385650635})
store['active_learning_steps'][45]['training']['best_epoch']=1
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8329, 'crossentropy': 0.93745791015625}
store['active_learning_steps'][45]['acquisition']={'indices': [55960, 4063, 15559, 39165, 9653], 'labels': [3, 8, 0, 6, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8980695009231567})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.0577070713043213})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.157930612564087})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.3156938552856445})
store['active_learning_steps'][46]['training']['best_epoch']=1
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8403, 'crossentropy': 0.87444404296875}
store['active_learning_steps'][46]['acquisition']={'indices': [18884, 27500, 55512, 32184, 59147], 'labels': [-1, 5, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9488059282302856})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.0202258825302124})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.122962236404419})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.2483935356140137})
store['active_learning_steps'][47]['training']['best_epoch']=1
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8358, 'crossentropy': 0.85250859375}
store['active_learning_steps'][47]['acquisition']={'indices': [13076, 48434, 43715, 57683, 9049], 'labels': [0, 0, 1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9582887291908264})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.1495208740234375})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.3004889488220215})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.3611292839050293})
store['active_learning_steps'][48]['training']['best_epoch']=1
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8392, 'crossentropy': 0.84961328125}
store['active_learning_steps'][48]['acquisition']={'indices': [29237, 31470, 49448, 25169, 27911], 'labels': [3, -1, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.902717113494873})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.065412998199463})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0588141679763794})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.1774177551269531})
store['active_learning_steps'][49]['training']['best_epoch']=1
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8521, 'crossentropy': 0.76467138671875}
store['active_learning_steps'][49]['acquisition']={'indices': [58193, 8391, 48630, 36004, 18802], 'labels': [5, 8, 6, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9639464616775513})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.064396858215332})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0589449405670166})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.1988732814788818})
store['active_learning_steps'][50]['training']['best_epoch']=1
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8396, 'crossentropy': 0.88489951171875}
store['active_learning_steps'][50]['acquisition']={'indices': [59723, 33928, 44864, 27410, 2634], 'labels': [0, 5, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9454248547554016})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9180805683135986})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9753877520561218})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.0921419858932495})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.225123405456543})
store['active_learning_steps'][51]['training']['best_epoch']=2
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8582, 'crossentropy': 0.9008123046875}
store['active_learning_steps'][51]['acquisition']={'indices': [6184, 14659, 20361, 4810, 31475], 'labels': [-1, -1, 1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8407502770423889})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8195184469223022})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0326340198516846})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 1.0097473859786987})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.0422005653381348})
store['active_learning_steps'][52]['training']['best_epoch']=2
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.8892, 'crossentropy': 0.741813818359375}
store['active_learning_steps'][52]['acquisition']={'indices': [474, 47999, 26806, 14802, 52755], 'labels': [5, 2, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7942016124725342})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8557772040367126})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9411767721176147})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9931398630142212})
store['active_learning_steps'][53]['training']['best_epoch']=1
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8678, 'crossentropy': 0.75138701171875}
store['active_learning_steps'][53]['acquisition']={'indices': [57882, 22981, 47599, 11690, 28502], 'labels': [-1, 0, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8052269220352173})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8371372222900391})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8882197141647339})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 1.0364797115325928})
store['active_learning_steps'][54]['training']['best_epoch']=1
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8649, 'crossentropy': 0.763684814453125}
store['active_learning_steps'][54]['acquisition']={'indices': [12899, 41879, 12274, 45444, 44904], 'labels': [8, 1, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.8726754784584045})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8896303176879883})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8829577565193176})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0372521877288818})
store['active_learning_steps'][55]['training']['best_epoch']=1
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.8353, 'crossentropy': 0.78800009765625}
store['active_learning_steps'][55]['acquisition']={'indices': [16686, 58821, 17566, 21165, 9329], 'labels': [-1, 2, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7088085412979126})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7232249975204468})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8702031373977661})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9017646312713623})
store['active_learning_steps'][56]['training']['best_epoch']=1
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8711, 'crossentropy': 0.69124873046875}
store['active_learning_steps'][56]['acquisition']={'indices': [20681, 22175, 7435, 14870, 30505], 'labels': [0, -1, 1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7818988561630249})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8015341758728027})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8148527145385742})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.925905168056488})
store['active_learning_steps'][57]['training']['best_epoch']=1
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8506, 'crossentropy': 0.774465185546875}
store['active_learning_steps'][57]['acquisition']={'indices': [8445, 46860, 46789, 45249, 32319], 'labels': [1, 0, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8562608957290649})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7345786094665527})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9073244333267212})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8618438243865967})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9375965595245361})
store['active_learning_steps'][58]['training']['best_epoch']=2
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.8939, 'crossentropy': 0.66967412109375}
store['active_learning_steps'][58]['acquisition']={'indices': [29836, 23161, 18008, 33949, 9615], 'labels': [6, 8, 4, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8290074467658997})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8219811916351318})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9234057664871216})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0265611410140991})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.1110856533050537})
store['active_learning_steps'][59]['training']['best_epoch']=2
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.8918, 'crossentropy': 0.7095908203125}
store['active_learning_steps'][59]['acquisition']={'indices': [10620, 47604, 58607, 10252, 11277], 'labels': [-1, 7, 8, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7629884481430054})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8702027797698975})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8083177804946899})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9057438373565674})
store['active_learning_steps'][60]['training']['best_epoch']=1
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8735, 'crossentropy': 0.6845916015625}
store['active_learning_steps'][60]['acquisition']={'indices': [8104, 31503, 29608, 58673, 39931], 'labels': [-1, -1, -1, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7179500460624695})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7519858479499817})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8272335529327393})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9561183452606201})
store['active_learning_steps'][61]['training']['best_epoch']=1
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.8826, 'crossentropy': 0.681619091796875}
store['active_learning_steps'][61]['acquisition']={'indices': [9878, 38852, 58451, 13829, 40945], 'labels': [-1, -1, -1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8162035942077637})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7691738605499268})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.761256992816925})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.821631133556366})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8741941452026367})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9620044827461243})
store['active_learning_steps'][62]['training']['best_epoch']=3
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9009, 'crossentropy': 0.680765576171875}
store['active_learning_steps'][62]['acquisition']={'indices': [28987, 5534, 56859, 53171, 24982], 'labels': [8, 8, 9, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8439297676086426})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7842321991920471})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8156304359436035})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8674831390380859})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.969818115234375})
store['active_learning_steps'][63]['training']['best_epoch']=2
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.8951, 'crossentropy': 0.682655224609375}
store['active_learning_steps'][63]['acquisition']={'indices': [23223, 11451, 20477, 18414, 18062], 'labels': [6, -1, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8984688520431519})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8146874308586121})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7469054460525513})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9400948286056519})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8642674684524536})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8247336149215698})
store['active_learning_steps'][64]['training']['best_epoch']=3
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.8933, 'crossentropy': 0.7718724609375}
store['active_learning_steps'][64]['acquisition']={'indices': [16774, 17337, 35776, 59165, 29035], 'labels': [3, 1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7177770733833313})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7299902439117432})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8738216161727905})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.9057378768920898})
store['active_learning_steps'][65]['training']['best_epoch']=1
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.8672, 'crossentropy': 0.717903759765625}
store['active_learning_steps'][65]['acquisition']={'indices': [13806, 8353, 56792, 51839, 6948], 'labels': [9, 7, 9, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7777004241943359})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7398520112037659})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8053072690963745})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8721036911010742})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9351669549942017})
store['active_learning_steps'][66]['training']['best_epoch']=2
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.8897, 'crossentropy': 0.684402294921875}
store['active_learning_steps'][66]['acquisition']={'indices': [36866, 28645, 52855, 44433, 51705], 'labels': [-1, 9, -1, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7381939888000488})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7649575471878052})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8280608654022217})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8475278615951538})
store['active_learning_steps'][67]['training']['best_epoch']=1
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.885, 'crossentropy': 0.6495919921875}
store['active_learning_steps'][67]['acquisition']={'indices': [6083, 40848, 8788, 25316, 28110], 'labels': [-1, -1, 0, 6, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7811679840087891})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8165236115455627})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8906311988830566})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.806208610534668})
store['active_learning_steps'][68]['training']['best_epoch']=1
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.8684, 'crossentropy': 0.7363908203125}
store['active_learning_steps'][68]['acquisition']={'indices': [3030, 47130, 6099, 34120, 55374], 'labels': [9, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7408444881439209})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6989501714706421})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8041199445724487})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8052158355712891})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8502486348152161})
store['active_learning_steps'][69]['training']['best_epoch']=2
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9033, 'crossentropy': 0.62462431640625}
store['active_learning_steps'][69]['acquisition']={'indices': [41599, 47899, 54929, 539, 45917], 'labels': [9, -1, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7673724293708801})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8334064483642578})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8524078130722046})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8058042526245117})
store['active_learning_steps'][70]['training']['best_epoch']=1
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.8657, 'crossentropy': 0.728289794921875}
store['active_learning_steps'][70]['acquisition']={'indices': [11803, 22657, 2327, 52722, 39411], 'labels': [6, 0, 0, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.738339364528656})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7479146718978882})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.753804087638855})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8008381128311157})
store['active_learning_steps'][71]['training']['best_epoch']=1
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.8763, 'crossentropy': 0.705384765625}
store['active_learning_steps'][71]['acquisition']={'indices': [49443, 16658, 8378, 32006, 30020], 'labels': [-1, 8, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7572122812271118})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7187111377716064})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7846776247024536})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.736758828163147})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.797587513923645})
store['active_learning_steps'][72]['training']['best_epoch']=2
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.8909, 'crossentropy': 0.688992138671875}
store['active_learning_steps'][72]['acquisition']={'indices': [56864, 43130, 52067, 8291, 35075], 'labels': [-1, 4, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8030604124069214})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7355509996414185})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8700298070907593})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8466765880584717})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9753957986831665})
store['active_learning_steps'][73]['training']['best_epoch']=2
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.8921, 'crossentropy': 0.675426513671875}
store['active_learning_steps'][73]['acquisition']={'indices': [56805, 53045, 32722, 43944, 51586], 'labels': [6, -1, 8, 8, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7077599167823792})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7340824604034424})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7435154914855957})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8752741813659668})
store['active_learning_steps'][74]['training']['best_epoch']=1
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.869, 'crossentropy': 0.67383134765625}
store['active_learning_steps'][74]['acquisition']={'indices': [34627, 1505, 39833, 44053, 27516], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.709092915058136})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7725633978843689})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7529809474945068})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7740826606750488})
store['active_learning_steps'][75]['training']['best_epoch']=1
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.8898, 'crossentropy': 0.66564501953125}
store['active_learning_steps'][75]['acquisition']={'indices': [14760, 2086, 50433, 45465, 55053], 'labels': [-1, 1, -1, 9, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7843619585037231})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6646209359169006})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7496551275253296})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8115875124931335})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8358672857284546})
store['active_learning_steps'][76]['training']['best_epoch']=2
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9027, 'crossentropy': 0.620079833984375}
store['active_learning_steps'][76]['acquisition']={'indices': [16509, 17741, 30818, 59660, 17916], 'labels': [-1, -1, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.671648383140564})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7118275165557861})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7612746953964233})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7689026594161987})
store['active_learning_steps'][77]['training']['best_epoch']=1
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.8756, 'crossentropy': 0.682114892578125}
store['active_learning_steps'][77]['acquisition']={'indices': [54658, 51156, 41068, 33651, 25181], 'labels': [-1, 9, -1, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6993013620376587})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7120382785797119})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7650545835494995})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8657567501068115})
store['active_learning_steps'][78]['training']['best_epoch']=1
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.8653, 'crossentropy': 0.7221869140625}
store['active_learning_steps'][78]['acquisition']={'indices': [59121, 39177, 25307, 6289, 5347], 'labels': [6, 6, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7091062068939209})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7351933121681213})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7101783752441406})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7555326223373413})
store['active_learning_steps'][79]['training']['best_epoch']=1
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.8715, 'crossentropy': 0.71207666015625}
store['active_learning_steps'][79]['acquisition']={'indices': [4702, 20315, 23430, 56890, 23788], 'labels': [6, -1, 7, 5, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7556632161140442})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7164920568466187})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7922540903091431})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7743171453475952})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8829487562179565})
store['active_learning_steps'][80]['training']['best_epoch']=2
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.8893, 'crossentropy': 0.66421015625}
store['active_learning_steps'][80]['acquisition']={'indices': [25592, 45164, 319, 17377, 47072], 'labels': [-1, 3, -1, 9, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7246475219726562})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7956457138061523})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8080426454544067})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7678725719451904})
store['active_learning_steps'][81]['training']['best_epoch']=1
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.846, 'crossentropy': 0.754732568359375}
store['active_learning_steps'][81]['acquisition']={'indices': [36120, 47519, 22681, 25962, 41209], 'labels': [-1, 3, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6727259755134583})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6895541548728943})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6600531339645386})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6822404265403748})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7723259925842285})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6726721525192261})
store['active_learning_steps'][82]['training']['best_epoch']=3
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9064, 'crossentropy': 0.6267650390625}
store['active_learning_steps'][82]['acquisition']={'indices': [33639, 38357, 40732, 5256, 41614], 'labels': [-1, 1, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7703611254692078})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6671425700187683})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.669770359992981})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7444671392440796})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7685531377792358})
store['active_learning_steps'][83]['training']['best_epoch']=2
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.8932, 'crossentropy': 0.62743076171875}
store['active_learning_steps'][83]['acquisition']={'indices': [14495, 57334, 39661, 37504, 35148], 'labels': [-1, -1, 1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6893835067749023})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7201225757598877})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7640240788459778})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7307043075561523})
store['active_learning_steps'][84]['training']['best_epoch']=1
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.8769, 'crossentropy': 0.668654150390625}
store['active_learning_steps'][84]['acquisition']={'indices': [14702, 42756, 54192, 45481, 23992], 'labels': [2, 5, 8, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7257508039474487})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.710709810256958})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6831142902374268})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6696969270706177})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7800966501235962})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7967805862426758})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7958357930183411})
store['active_learning_steps'][85]['training']['best_epoch']=4
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9105, 'crossentropy': 0.596454541015625}
store['active_learning_steps'][85]['acquisition']={'indices': [38083, 5404, 15572, 35776, 32553], 'labels': [3, -1, -1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7109489440917969})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.615228533744812})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6981970071792603})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7476096153259277})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8127238750457764})
store['active_learning_steps'][86]['training']['best_epoch']=2
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9056, 'crossentropy': 0.5963755859375}
store['active_learning_steps'][86]['acquisition']={'indices': [33798, 21785, 222, 10204, 54029], 'labels': [7, -1, 4, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7714234590530396})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6783874034881592})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6338678598403931})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6192196607589722})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7846046090126038})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7215094566345215})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7952237129211426})
store['active_learning_steps'][87]['training']['best_epoch']=4
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.9135, 'crossentropy': 0.588279150390625}
store['active_learning_steps'][87]['acquisition']={'indices': [25482, 10870, 2028, 45146, 14829], 'labels': [8, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7667596340179443})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6854722499847412})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7910107374191284})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7426435947418213})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7441630363464355})
store['active_learning_steps'][88]['training']['best_epoch']=2
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.8919, 'crossentropy': 0.641799462890625}
store['active_learning_steps'][88]['acquisition']={'indices': [10353, 24845, 30095, 35755, 9174], 'labels': [-1, -1, 9, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7344779968261719})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6620879173278809})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6877297759056091})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6888124942779541})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7280375957489014})
store['active_learning_steps'][89]['training']['best_epoch']=2
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.897, 'crossentropy': 0.58994873046875}
store['active_learning_steps'][89]['acquisition']={'indices': [35019, 18300, 6523, 51563, 45898], 'labels': [-1, -1, 8, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6842036247253418})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.659140944480896})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6608405113220215})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7121410369873047})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8300884962081909})
store['active_learning_steps'][90]['training']['best_epoch']=2
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.8998, 'crossentropy': 0.584685546875}
store['active_learning_steps'][90]['acquisition']={'indices': [56290, 58210, 38711, 23529, 32572], 'labels': [8, -1, -1, 4, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7184881567955017})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7261363863945007})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7474315166473389})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6673988103866577})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7054365873336792})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6766530275344849})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.7591246366500854})
store['active_learning_steps'][91]['training']['best_epoch']=4
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.9148, 'crossentropy': 0.631102783203125}
store['active_learning_steps'][91]['acquisition']={'indices': [7238, 30608, 54789, 8374, 25062], 'labels': [5, 6, 7, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7401509284973145})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.665622353553772})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6057056188583374})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6407876014709473})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8077468276023865})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6963289380073547})
store['active_learning_steps'][92]['training']['best_epoch']=3
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.9148, 'crossentropy': 0.56244951171875}
store['active_learning_steps'][92]['acquisition']={'indices': [41471, 35963, 40003, 42399, 33067], 'labels': [3, -1, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7300320863723755})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6573541164398193})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6371880769729614})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6692081093788147})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7007015943527222})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7135067582130432})
store['active_learning_steps'][93]['training']['best_epoch']=3
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.9119, 'crossentropy': 0.556133740234375}
store['active_learning_steps'][93]['acquisition']={'indices': [24471, 18465, 22179, 27529, 6559], 'labels': [4, 6, 1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7778888940811157})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6358215808868408})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6002769470214844})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6359832286834717})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6219583749771118})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7171356678009033})
store['active_learning_steps'][94]['training']['best_epoch']=3
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.9141, 'crossentropy': 0.5613173828125}
store['active_learning_steps'][94]['acquisition']={'indices': [17973, 1118, 38893, 5285, 57743], 'labels': [-1, 1, 0, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6955485343933105})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6265500783920288})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6574596762657166})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6708019971847534})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7560603618621826})
store['active_learning_steps'][95]['training']['best_epoch']=2
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.9071, 'crossentropy': 0.557159423828125}
store['active_learning_steps'][95]['acquisition']={'indices': [57845, 46711, 24160, 13556, 33481], 'labels': [-1, -1, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6930019855499268})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6508055925369263})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7650113105773926})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6913497447967529})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7442805767059326})
store['active_learning_steps'][96]['training']['best_epoch']=2
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.9009, 'crossentropy': 0.59517685546875}
store['active_learning_steps'][96]['acquisition']={'indices': [7805, 22946, 7962, 2342, 8949], 'labels': [-1, -1, 5, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7142406702041626})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6003971695899963})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6241808533668518})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5591099262237549})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6754772663116455})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6838700771331787})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7351282835006714})
store['active_learning_steps'][97]['training']['best_epoch']=4
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.9243, 'crossentropy': 0.5408666015625}
store['active_learning_steps'][97]['acquisition']={'indices': [38599, 34959, 56972, 7524, 40423], 'labels': [0, -1, 6, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6482789516448975})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.580112636089325})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6544738411903381})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6553863286972046})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6599134802818298})
store['active_learning_steps'][98]['training']['best_epoch']=2
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.9071, 'crossentropy': 0.54725693359375}
store['active_learning_steps'][98]['acquisition']={'indices': [15307, 50254, 42877, 44866, 480], 'labels': [8, -1, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7185229063034058})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5855967998504639})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5929228067398071})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.67741858959198})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6900750398635864})
store['active_learning_steps'][99]['training']['best_epoch']=2
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.9056, 'crossentropy': 0.542408203125}
store['active_learning_steps'][99]['acquisition']={'indices': [6560, 58341, 30279, 44478, 29690], 'labels': [-1, 1, 6, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7665215730667114})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6010103225708008})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7017287015914917})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6779198050498962})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.735806405544281})
store['active_learning_steps'][100]['training']['best_epoch']=2
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.9004, 'crossentropy': 0.575060693359375}
store['active_learning_steps'][100]['acquisition']={'indices': [6305, 14272, 41729, 12444, 34287], 'labels': [-1, -1, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][101]['training']={}
store['active_learning_steps'][101]['training']['epochs']=[]
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.649885892868042})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6524813175201416})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6442419290542603})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5799652934074402})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6164757013320923})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6704006791114807})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6910232305526733})
store['active_learning_steps'][101]['training']['best_epoch']=4
store['active_learning_steps'][101]['evaluation_metrics']={'accuracy': 0.9247, 'crossentropy': 0.538822998046875}
store['active_learning_steps'][101]['acquisition']={'indices': [38730, 1355, 37536, 18163, 47566], 'labels': [-1, -1, -1, 1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][102]['training']={}
store['active_learning_steps'][102]['training']['epochs']=[]
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6935871839523315})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6215643286705017})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5370757579803467})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6934008598327637})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6733373403549194})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5992372035980225})
store['active_learning_steps'][102]['training']['best_epoch']=3
store['active_learning_steps'][102]['evaluation_metrics']={'accuracy': 0.9185, 'crossentropy': 0.518810595703125}
store['active_learning_steps'][102]['acquisition']={'indices': [55475, 45004, 44832, 29652, 38634], 'labels': [-1, -1, 7, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][103]['training']={}
store['active_learning_steps'][103]['training']['epochs']=[]
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.682546854019165})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.563746988773346})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5995751619338989})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.602272629737854})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6633080244064331})
store['active_learning_steps'][103]['training']['best_epoch']=2
store['active_learning_steps'][103]['evaluation_metrics']={'accuracy': 0.912, 'crossentropy': 0.52776875}
store['active_learning_steps'][103]['acquisition']={'indices': [21257, 57228, 22573, 43405, 21889], 'labels': [6, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][104]['training']={}
store['active_learning_steps'][104]['training']['epochs']=[]
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7269548773765564})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6326906681060791})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6483449935913086})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6497851014137268})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6660810112953186})
store['active_learning_steps'][104]['training']['best_epoch']=2
store['active_learning_steps'][104]['evaluation_metrics']={'accuracy': 0.9094, 'crossentropy': 0.544587841796875}
store['active_learning_steps'][104]['acquisition']={'indices': [42944, 19941, 53877, 31523, 30069], 'labels': [8, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][105]['training']={}
store['active_learning_steps'][105]['training']['epochs']=[]
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6947571039199829})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6290032267570496})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6391929984092712})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7184092998504639})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.684160590171814})
store['active_learning_steps'][105]['training']['best_epoch']=2
store['active_learning_steps'][105]['evaluation_metrics']={'accuracy': 0.9029, 'crossentropy': 0.56508720703125}
store['active_learning_steps'][105]['acquisition']={'indices': [49372, 9841, 47759, 57249, 37558], 'labels': [-1, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][106]['training']={}
store['active_learning_steps'][106]['training']['epochs']=[]
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7223244905471802})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6106259822845459})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6120121479034424})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7212741374969482})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6719275116920471})
store['active_learning_steps'][106]['training']['best_epoch']=2
store['active_learning_steps'][106]['evaluation_metrics']={'accuracy': 0.9092, 'crossentropy': 0.54649443359375}
store['active_learning_steps'][106]['acquisition']={'indices': [47982, 7976, 5834, 333, 32281], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][107]['training']={}
store['active_learning_steps'][107]['training']['epochs']=[]
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7479883432388306})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6231837272644043})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6385587453842163})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7057512998580933})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.738160252571106})
store['active_learning_steps'][107]['training']['best_epoch']=2
store['active_learning_steps'][107]['evaluation_metrics']={'accuracy': 0.9142, 'crossentropy': 0.559156494140625}
store['active_learning_steps'][107]['acquisition']={'indices': [56371, 5534, 5317, 5377, 10927], 'labels': [5, -1, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][108]['training']={}
store['active_learning_steps'][108]['training']['epochs']=[]
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6779423952102661})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6056613922119141})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6064097881317139})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.75386643409729})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7207900285720825})
store['active_learning_steps'][108]['training']['best_epoch']=2
store['active_learning_steps'][108]['evaluation_metrics']={'accuracy': 0.9095, 'crossentropy': 0.528383984375}
store['active_learning_steps'][108]['acquisition']={'indices': [9414, 31736, 8771, 13217, 42868], 'labels': [5, 6, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][109]['training']={}
store['active_learning_steps'][109]['training']['epochs']=[]
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6766284108161926})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5922340750694275})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6204760670661926})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6321665048599243})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6471327543258667})
store['active_learning_steps'][109]['training']['best_epoch']=2
store['active_learning_steps'][109]['evaluation_metrics']={'accuracy': 0.9054, 'crossentropy': 0.536952685546875}
store['active_learning_steps'][109]['acquisition']={'indices': [4608, 26962, 17440, 38815, 45190], 'labels': [-1, -1, 7, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][110]['training']={}
store['active_learning_steps'][110]['training']['epochs']=[]
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7032179832458496})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5475398302078247})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6777781844139099})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.585044264793396})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.676256537437439})
store['active_learning_steps'][110]['training']['best_epoch']=2
store['active_learning_steps'][110]['evaluation_metrics']={'accuracy': 0.9247, 'crossentropy': 0.499509912109375}
store['active_learning_steps'][110]['acquisition']={'indices': [20712, 29485, 46155, 30471, 23956], 'labels': [-1, 4, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][111]['training']={}
store['active_learning_steps'][111]['training']['epochs']=[]
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7199799418449402})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5615309476852417})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6099461317062378})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6799169182777405})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7284358739852905})
store['active_learning_steps'][111]['training']['best_epoch']=2
store['active_learning_steps'][111]['evaluation_metrics']={'accuracy': 0.9174, 'crossentropy': 0.507510205078125}
store['active_learning_steps'][111]['acquisition']={'indices': [13748, 56772, 9443, 26263, 27274], 'labels': [1, 1, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][112]['training']={}
store['active_learning_steps'][112]['training']['epochs']=[]
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6468289494514465})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6246354579925537})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6094500422477722})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5636388063430786})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7549973726272583})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6819720268249512})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6856918931007385})
store['active_learning_steps'][112]['training']['best_epoch']=4
store['active_learning_steps'][112]['evaluation_metrics']={'accuracy': 0.9227, 'crossentropy': 0.5186384765625}
store['active_learning_steps'][112]['acquisition']={'indices': [27363, 15636, 2462, 21913, 26928], 'labels': [-1, 8, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][113]['training']={}
store['active_learning_steps'][113]['training']['epochs']=[]
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7012357711791992})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5959397554397583})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.634760856628418})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7004764676094055})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7278066873550415})
store['active_learning_steps'][113]['training']['best_epoch']=2
store['active_learning_steps'][113]['evaluation_metrics']={'accuracy': 0.9076, 'crossentropy': 0.542799365234375}
store['active_learning_steps'][113]['acquisition']={'indices': [41095, 46657, 20015, 13346, 45798], 'labels': [7, 8, -1, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][114]['training']={}
store['active_learning_steps'][114]['training']['epochs']=[]
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6991517543792725})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6339128017425537})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5432562828063965})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6011371612548828})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5733267068862915})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6601840257644653})
store['active_learning_steps'][114]['training']['best_epoch']=3
store['active_learning_steps'][114]['evaluation_metrics']={'accuracy': 0.9202, 'crossentropy': 0.51063212890625}
store['active_learning_steps'][114]['acquisition']={'indices': [53602, 4433, 31149, 53508, 40078], 'labels': [4, -1, 5, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][115]['training']={}
store['active_learning_steps'][115]['training']['epochs']=[]
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7079011797904968})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5288883447647095})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5814103484153748})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.535069465637207})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6388273239135742})
store['active_learning_steps'][115]['training']['best_epoch']=2
store['active_learning_steps'][115]['evaluation_metrics']={'accuracy': 0.9107, 'crossentropy': 0.5237134765625}
store['active_learning_steps'][115]['acquisition']={'indices': [47773, 12040, 6802, 26899, 157], 'labels': [-1, -1, 0, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][116]['training']={}
store['active_learning_steps'][116]['training']['epochs']=[]
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7146905064582825})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5505661368370056})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5860884189605713})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5853294134140015})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6436970233917236})
store['active_learning_steps'][116]['training']['best_epoch']=2
store['active_learning_steps'][116]['evaluation_metrics']={'accuracy': 0.9181, 'crossentropy': 0.51646630859375}
store['active_learning_steps'][116]['acquisition']={'indices': [33586, 31713, 25870, 42743, 37561], 'labels': [1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][117]['training']={}
store['active_learning_steps'][117]['training']['epochs']=[]
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.6955751180648804})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6096814870834351})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5943445563316345})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6355099678039551})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6341990232467651})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7048664093017578})
store['active_learning_steps'][117]['training']['best_epoch']=3
store['active_learning_steps'][117]['evaluation_metrics']={'accuracy': 0.9112, 'crossentropy': 0.523063037109375}
store['active_learning_steps'][117]['acquisition']={'indices': [50865, 42511, 45472, 50243, 11833], 'labels': [6, -1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][118]['training']={}
store['active_learning_steps'][118]['training']['epochs']=[]
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6520481109619141})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.62236487865448})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.619636058807373})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6299254894256592})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6833497285842896})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7031341791152954})
store['active_learning_steps'][118]['training']['best_epoch']=3
store['active_learning_steps'][118]['evaluation_metrics']={'accuracy': 0.91, 'crossentropy': 0.556071875}
store['active_learning_steps'][118]['acquisition']={'indices': [49150, 47381, 19881, 10976, 17850], 'labels': [-1, -1, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][119]['training']={}
store['active_learning_steps'][119]['training']['epochs']=[]
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7070279717445374})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5645090341567993})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6186081171035767})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6183416843414307})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6996673345565796})
store['active_learning_steps'][119]['training']['best_epoch']=2
store['active_learning_steps'][119]['evaluation_metrics']={'accuracy': 0.908, 'crossentropy': 0.542937451171875}
store['active_learning_steps'][119]['acquisition']={'indices': [16692, 31359, 37319, 32450, 8876], 'labels': [5, 4, 8, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][120]['training']={}
store['active_learning_steps'][120]['training']['epochs']=[]
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7269183993339539})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6208829879760742})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5505776405334473})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6234797835350037})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6773528456687927})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6493811011314392})
store['active_learning_steps'][120]['training']['best_epoch']=3
store['active_learning_steps'][120]['evaluation_metrics']={'accuracy': 0.9149, 'crossentropy': 0.524592822265625}
store['active_learning_steps'][120]['acquisition']={'indices': [59727, 22025, 11910, 49126, 33723], 'labels': [4, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][121]['training']={}
store['active_learning_steps'][121]['training']['epochs']=[]
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6639697551727295})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5804025530815125})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5654728412628174})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6430738568305969})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5986950993537903})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7769792079925537})
store['active_learning_steps'][121]['training']['best_epoch']=3
store['active_learning_steps'][121]['evaluation_metrics']={'accuracy': 0.9114, 'crossentropy': 0.52388701171875}
store['active_learning_steps'][121]['acquisition']={'indices': [5234, 53589, 34423, 8914, 43603], 'labels': [1, 7, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][122]['training']={}
store['active_learning_steps'][122]['training']['epochs']=[]
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6521211862564087})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5804369449615479})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5587054491043091})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5516967177391052})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6285122632980347})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6270442008972168})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6343899965286255})
store['active_learning_steps'][122]['training']['best_epoch']=4
store['active_learning_steps'][122]['evaluation_metrics']={'accuracy': 0.9241, 'crossentropy': 0.48794892578125}
store['active_learning_steps'][122]['acquisition']={'indices': [26679, 39284, 27464, 44700, 34585], 'labels': [-1, 2, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][123]['training']={}
store['active_learning_steps'][123]['training']['epochs']=[]
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7588274478912354})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6130330562591553})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5235574245452881})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5640369653701782})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5854342579841614})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6880520582199097})
store['active_learning_steps'][123]['training']['best_epoch']=3
store['active_learning_steps'][123]['evaluation_metrics']={'accuracy': 0.9184, 'crossentropy': 0.500594775390625}
store['active_learning_steps'][123]['acquisition']={'indices': [8104, 47859, 52874, 50389, 18137], 'labels': [5, -1, 2, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][124]['training']={}
store['active_learning_steps'][124]['training']['epochs']=[]
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6713418960571289})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5671457052230835})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5796526670455933})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7202759385108948})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5701078176498413})
store['active_learning_steps'][124]['training']['best_epoch']=2
store['active_learning_steps'][124]['evaluation_metrics']={'accuracy': 0.9077, 'crossentropy': 0.520525927734375}
store['active_learning_steps'][124]['acquisition']={'indices': [33817, 5641, 48043, 48139, 2174], 'labels': [-1, -1, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][125]['training']={}
store['active_learning_steps'][125]['training']['epochs']=[]
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7426841855049133})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5947341918945312})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.583420991897583})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6641115546226501})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6721281409263611})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6754223108291626})
store['active_learning_steps'][125]['training']['best_epoch']=3
store['active_learning_steps'][125]['evaluation_metrics']={'accuracy': 0.912, 'crossentropy': 0.54496201171875}
store['active_learning_steps'][125]['acquisition']={'indices': [28881, 49790, 20722, 2551, 48829], 'labels': [3, -1, 8, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][126]['training']={}
store['active_learning_steps'][126]['training']['epochs']=[]
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7158364057540894})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6022630929946899})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5666989684104919})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6555933952331543})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.629602313041687})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6885809302330017})
store['active_learning_steps'][126]['training']['best_epoch']=3
store['active_learning_steps'][126]['evaluation_metrics']={'accuracy': 0.917, 'crossentropy': 0.524847021484375}
store['active_learning_steps'][126]['acquisition']={'indices': [56256, 37747, 26833, 59423, 39706], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][127]['training']={}
store['active_learning_steps'][127]['training']['epochs']=[]
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6244677305221558})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5162936449050903})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5269244909286499})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5635327100753784})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5446171760559082})
store['active_learning_steps'][127]['training']['best_epoch']=2
store['active_learning_steps'][127]['evaluation_metrics']={'accuracy': 0.9195, 'crossentropy': 0.4815380859375}
store['active_learning_steps'][127]['acquisition']={'indices': [46595, 31122, 42848, 31190, 55181], 'labels': [-1, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][128]['training']={}
store['active_learning_steps'][128]['training']['epochs']=[]
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7003845572471619})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5800868272781372})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5808889865875244})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5683139562606812})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6594407558441162})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6332191228866577})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.7179217338562012})
store['active_learning_steps'][128]['training']['best_epoch']=4
store['active_learning_steps'][128]['evaluation_metrics']={'accuracy': 0.9202, 'crossentropy': 0.518317578125}
store['active_learning_steps'][128]['acquisition']={'indices': [35895, 15628, 26066, 3633, 12525], 'labels': [4, -1, 5, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][129]['training']={}
store['active_learning_steps'][129]['training']['epochs']=[]
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6818443536758423})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5672290325164795})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6130806803703308})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5716922879219055})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5818092823028564})
store['active_learning_steps'][129]['training']['best_epoch']=2
store['active_learning_steps'][129]['evaluation_metrics']={'accuracy': 0.9073, 'crossentropy': 0.53346708984375}
store['active_learning_steps'][129]['acquisition']={'indices': [46212, 30584, 52661, 40863, 3392], 'labels': [-1, -1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][130]['training']={}
store['active_learning_steps'][130]['training']['epochs']=[]
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7506254315376282})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5438939332962036})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5946314334869385})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6147387623786926})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6287533044815063})
store['active_learning_steps'][130]['training']['best_epoch']=2
store['active_learning_steps'][130]['evaluation_metrics']={'accuracy': 0.9117, 'crossentropy': 0.503919677734375}
store['active_learning_steps'][130]['acquisition']={'indices': [14131, 3480, 1538, 43907, 46534], 'labels': [0, 8, -1, 8, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][131]['training']={}
store['active_learning_steps'][131]['training']['epochs']=[]
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6260910034179688})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5658528804779053})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.574926495552063})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6421641111373901})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6789000034332275})
store['active_learning_steps'][131]['training']['best_epoch']=2
store['active_learning_steps'][131]['evaluation_metrics']={'accuracy': 0.9088, 'crossentropy': 0.535647265625}
store['active_learning_steps'][131]['acquisition']={'indices': [40015, 41049, 46903, 28062, 1645], 'labels': [-1, 5, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][132]['training']={}
store['active_learning_steps'][132]['training']['epochs']=[]
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6303367614746094})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5595623850822449})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6297160387039185})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5627480149269104})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5940265655517578})
store['active_learning_steps'][132]['training']['best_epoch']=2
store['active_learning_steps'][132]['evaluation_metrics']={'accuracy': 0.9128, 'crossentropy': 0.503223095703125}
store['active_learning_steps'][132]['acquisition']={'indices': [46026, 26822, 529, 24096, 43801], 'labels': [-1, 9, 9, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][133]['training']={}
store['active_learning_steps'][133]['training']['epochs']=[]
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6930683255195618})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5619708895683289})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5969827771186829})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6043816208839417})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6566088795661926})
store['active_learning_steps'][133]['training']['best_epoch']=2
store['active_learning_steps'][133]['evaluation_metrics']={'accuracy': 0.914, 'crossentropy': 0.499097900390625}
store['active_learning_steps'][133]['acquisition']={'indices': [55481, 36992, 57247, 28512, 36048], 'labels': [0, 1, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][134]['training']={}
store['active_learning_steps'][134]['training']['epochs']=[]
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6654846668243408})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5880777835845947})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5719773769378662})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6260794401168823})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5854887962341309})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6630584001541138})
store['active_learning_steps'][134]['training']['best_epoch']=3
store['active_learning_steps'][134]['evaluation_metrics']={'accuracy': 0.9166, 'crossentropy': 0.52316416015625}
store['active_learning_steps'][134]['acquisition']={'indices': [20224, 7893, 43247, 31990, 55604], 'labels': [-1, -1, 0, 1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][135]['training']={}
store['active_learning_steps'][135]['training']['epochs']=[]
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.674958348274231})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5052626132965088})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5406579971313477})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5592840313911438})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5580826997756958})
store['active_learning_steps'][135]['training']['best_epoch']=2
store['active_learning_steps'][135]['evaluation_metrics']={'accuracy': 0.9159, 'crossentropy': 0.4723140625}
store['active_learning_steps'][135]['acquisition']={'indices': [49472, 57025, 27051, 6960, 1708], 'labels': [-1, -1, -1, 0, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][136]['training']={}
store['active_learning_steps'][136]['training']['epochs']=[]
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.743545651435852})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6425712704658508})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.671960711479187})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7530412673950195})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6868678331375122})
store['active_learning_steps'][136]['training']['best_epoch']=2
store['active_learning_steps'][136]['evaluation_metrics']={'accuracy': 0.8899, 'crossentropy': 0.614344921875}
store['active_learning_steps'][136]['acquisition']={'indices': [5246, 43717, 18967, 40321, 1784], 'labels': [-1, -1, -1, 2, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][137]['training']={}
store['active_learning_steps'][137]['training']['epochs']=[]
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6759729385375977})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5464034676551819})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5782802104949951})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5645507574081421})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5834911465644836})
store['active_learning_steps'][137]['training']['best_epoch']=2
store['active_learning_steps'][137]['evaluation_metrics']={'accuracy': 0.9091, 'crossentropy': 0.515777294921875}
store['active_learning_steps'][137]['acquisition']={'indices': [17828, 5347, 59196, 51411, 4528], 'labels': [0, 7, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][138]['training']={}
store['active_learning_steps'][138]['training']['epochs']=[]
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6164291501045227})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5338695049285889})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5365877151489258})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5819764733314514})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6344289183616638})
store['active_learning_steps'][138]['training']['best_epoch']=2
store['active_learning_steps'][138]['evaluation_metrics']={'accuracy': 0.9118, 'crossentropy': 0.533106103515625}
store['active_learning_steps'][138]['acquisition']={'indices': [23224, 27387, 6414, 27995, 27543], 'labels': [-1, 9, 2, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][139]['training']={}
store['active_learning_steps'][139]['training']['epochs']=[]
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.756207287311554})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5403903722763062})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6103411912918091})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5523579120635986})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5654759407043457})
store['active_learning_steps'][139]['training']['best_epoch']=2
store['active_learning_steps'][139]['evaluation_metrics']={'accuracy': 0.9137, 'crossentropy': 0.5069884765625}
store['active_learning_steps'][139]['acquisition']={'indices': [10814, 40475, 14715, 47953, 28844], 'labels': [5, 6, -1, 0, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][140]['training']={}
store['active_learning_steps'][140]['training']['epochs']=[]
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7076562643051147})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5783299803733826})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5672043561935425})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5599526762962341})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6404361128807068})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6400530338287354})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6452292203903198})
store['active_learning_steps'][140]['training']['best_epoch']=4
store['active_learning_steps'][140]['evaluation_metrics']={'accuracy': 0.9215, 'crossentropy': 0.491202880859375}
store['active_learning_steps'][140]['acquisition']={'indices': [17591, 27079, 11947, 29077, 37424], 'labels': [9, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][141]['training']={}
store['active_learning_steps'][141]['training']['epochs']=[]
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6390601396560669})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5002439618110657})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5275543928146362})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6030977964401245})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.581733226776123})
store['active_learning_steps'][141]['training']['best_epoch']=2
store['active_learning_steps'][141]['evaluation_metrics']={'accuracy': 0.9183, 'crossentropy': 0.483879150390625}
store['active_learning_steps'][141]['acquisition']={'indices': [20183, 44474, 56005, 13210, 24287], 'labels': [-1, -1, 0, 6, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][142]['training']={}
store['active_learning_steps'][142]['training']['epochs']=[]
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6870989799499512})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5806113481521606})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5273975133895874})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6141075491905212})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6049141883850098})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.687409520149231})
store['active_learning_steps'][142]['training']['best_epoch']=3
store['active_learning_steps'][142]['evaluation_metrics']={'accuracy': 0.9193, 'crossentropy': 0.479378271484375}
store['active_learning_steps'][142]['acquisition']={'indices': [23858, 7451, 33055, 31894, 18221], 'labels': [-1, -1, 6, 1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][143]['training']={}
store['active_learning_steps'][143]['training']['epochs']=[]
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.6815373301506042})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6313002109527588})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.584013044834137})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6176950931549072})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6346045732498169})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6185800433158875})
store['active_learning_steps'][143]['training']['best_epoch']=3
store['active_learning_steps'][143]['evaluation_metrics']={'accuracy': 0.9163, 'crossentropy': 0.528983203125}
store['active_learning_steps'][143]['acquisition']={'indices': [30919, 4171, 44898, 20761, 1834], 'labels': [-1, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][144]['training']={}
store['active_learning_steps'][144]['training']['epochs']=[]
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6519100666046143})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5113459825515747})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5009787678718567})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.613684892654419})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5751579999923706})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5989338159561157})
store['active_learning_steps'][144]['training']['best_epoch']=3
store['active_learning_steps'][144]['evaluation_metrics']={'accuracy': 0.9245, 'crossentropy': 0.443725830078125}
store['active_learning_steps'][144]['acquisition']={'indices': [6331, 19456, 1940, 37250, 10477], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][145]['training']={}
store['active_learning_steps'][145]['training']['epochs']=[]
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6757199764251709})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5803982019424438})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5586277842521667})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.572029709815979})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5935611724853516})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6932955980300903})
store['active_learning_steps'][145]['training']['best_epoch']=3
store['active_learning_steps'][145]['evaluation_metrics']={'accuracy': 0.916, 'crossentropy': 0.50441982421875}
store['active_learning_steps'][145]['acquisition']={'indices': [35203, 41664, 11824, 26518, 56412], 'labels': [7, 4, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][146]['training']={}
store['active_learning_steps'][146]['training']['epochs']=[]
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6911040544509888})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6290724277496338})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5952166318893433})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5977463126182556})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5723640322685242})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6215837001800537})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6722666025161743})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6680639982223511})
store['active_learning_steps'][146]['training']['best_epoch']=5
store['active_learning_steps'][146]['evaluation_metrics']={'accuracy': 0.927, 'crossentropy': 0.50878359375}
store['active_learning_steps'][146]['acquisition']={'indices': [58346, 8140, 28413, 57756, 40308], 'labels': [-1, -1, -1, 6, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][147]['training']={}
store['active_learning_steps'][147]['training']['epochs']=[]
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6722846031188965})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.544048547744751})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.520646333694458})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5594422817230225})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6047043800354004})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5585101842880249})
store['active_learning_steps'][147]['training']['best_epoch']=3
store['active_learning_steps'][147]['evaluation_metrics']={'accuracy': 0.9214, 'crossentropy': 0.508939794921875}
store['active_learning_steps'][147]['acquisition']={'indices': [14155, 40211, 27735, 53220, 45861], 'labels': [6, 7, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][148]['training']={}
store['active_learning_steps'][148]['training']['epochs']=[]
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6645591259002686})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5350511074066162})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5220909118652344})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.57725989818573})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5742201805114746})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.592439591884613})
store['active_learning_steps'][148]['training']['best_epoch']=3
store['active_learning_steps'][148]['evaluation_metrics']={'accuracy': 0.9226, 'crossentropy': 0.472681005859375}
store['active_learning_steps'][148]['acquisition']={'indices': [5765, 26049, 43464, 48455, 55664], 'labels': [-1, -1, 8, 8, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][149]['training']={}
store['active_learning_steps'][149]['training']['epochs']=[]
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7036609053611755})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.579180121421814})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5888592600822449})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6137657165527344})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6124184131622314})
store['active_learning_steps'][149]['training']['best_epoch']=2
store['active_learning_steps'][149]['evaluation_metrics']={'accuracy': 0.9014, 'crossentropy': 0.536854052734375}
store['active_learning_steps'][149]['acquisition']={'indices': [29558, 44395, 37417, 48619, 37663], 'labels': [4, -1, 8, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][150]['training']={}
store['active_learning_steps'][150]['training']['epochs']=[]
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6596639156341553})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.49731725454330444})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5562257766723633})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5091170072555542})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6022778749465942})
store['active_learning_steps'][150]['training']['best_epoch']=2
store['active_learning_steps'][150]['evaluation_metrics']={'accuracy': 0.9141, 'crossentropy': 0.466150732421875}
store['active_learning_steps'][150]['acquisition']={'indices': [22679, 36487, 17734, 25715, 21557], 'labels': [5, 5, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][151]['training']={}
store['active_learning_steps'][151]['training']['epochs']=[]
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6892436742782593})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5201793909072876})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5492367148399353})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5477126240730286})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5946655869483948})
store['active_learning_steps'][151]['training']['best_epoch']=2
store['active_learning_steps'][151]['evaluation_metrics']={'accuracy': 0.9098, 'crossentropy': 0.4662763671875}
store['active_learning_steps'][151]['acquisition']={'indices': [6587, 13873, 29869, 39844, 880], 'labels': [7, -1, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][152]['training']={}
store['active_learning_steps'][152]['training']['epochs']=[]
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7247219085693359})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5579167008399963})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6207756996154785})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6235971450805664})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5940940380096436})
store['active_learning_steps'][152]['training']['best_epoch']=2
store['active_learning_steps'][152]['evaluation_metrics']={'accuracy': 0.9139, 'crossentropy': 0.503920947265625}
store['active_learning_steps'][152]['acquisition']={'indices': [9310, 31404, 12675, 31641, 19892], 'labels': [0, 3, 4, 3, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][153]['training']={}
store['active_learning_steps'][153]['training']['epochs']=[]
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7066519856452942})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6371356248855591})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5305637121200562})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5899268388748169})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6529536247253418})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6265684366226196})
store['active_learning_steps'][153]['training']['best_epoch']=3
store['active_learning_steps'][153]['evaluation_metrics']={'accuracy': 0.9228, 'crossentropy': 0.46100986328125}
store['active_learning_steps'][153]['acquisition']={'indices': [4933, 27616, 47946, 19010, 45499], 'labels': [1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][154]['training']={}
store['active_learning_steps'][154]['training']['epochs']=[]
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6553345918655396})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5933340787887573})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5643508434295654})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5876543521881104})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.6059878468513489})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5654094219207764})
store['active_learning_steps'][154]['training']['best_epoch']=3
store['active_learning_steps'][154]['evaluation_metrics']={'accuracy': 0.9159, 'crossentropy': 0.502327294921875}
store['active_learning_steps'][154]['acquisition']={'indices': [23666, 40170, 31351, 14560, 34261], 'labels': [-1, 7, 9, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][155]['training']={}
store['active_learning_steps'][155]['training']['epochs']=[]
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7091532945632935})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5071195363998413})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6139864921569824})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5964044332504272})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5811433792114258})
store['active_learning_steps'][155]['training']['best_epoch']=2
store['active_learning_steps'][155]['evaluation_metrics']={'accuracy': 0.9053, 'crossentropy': 0.53134697265625}
store['active_learning_steps'][155]['acquisition']={'indices': [2236, 42346, 39464, 49729, 50584], 'labels': [-1, -1, 9, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][156]['training']={}
store['active_learning_steps'][156]['training']['epochs']=[]
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6623400449752808})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5291059613227844})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5352996587753296})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5325040221214294})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5900275707244873})
store['active_learning_steps'][156]['training']['best_epoch']=2
store['active_learning_steps'][156]['evaluation_metrics']={'accuracy': 0.9106, 'crossentropy': 0.4931232421875}
store['active_learning_steps'][156]['acquisition']={'indices': [10348, 13832, 7933, 29522, 42620], 'labels': [0, 6, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][157]['training']={}
store['active_learning_steps'][157]['training']['epochs']=[]
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7031246423721313})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5987964272499084})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5695909261703491})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6270688772201538})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5761839151382446})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.577214777469635})
store['active_learning_steps'][157]['training']['best_epoch']=3
store['active_learning_steps'][157]['evaluation_metrics']={'accuracy': 0.9166, 'crossentropy': 0.501489306640625}
store['active_learning_steps'][157]['acquisition']={'indices': [58896, 22058, 19351, 33430, 26010], 'labels': [2, -1, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][158]['training']={}
store['active_learning_steps'][158]['training']['epochs']=[]
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6476613283157349})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5755735039710999})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5436596274375916})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5853978991508484})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5792518854141235})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6469908952713013})
store['active_learning_steps'][158]['training']['best_epoch']=3
store['active_learning_steps'][158]['evaluation_metrics']={'accuracy': 0.918, 'crossentropy': 0.46542939453125}
store['active_learning_steps'][158]['acquisition']={'indices': [59160, 42749, 52893, 21446, 16363], 'labels': [-1, 8, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][159]['training']={}
store['active_learning_steps'][159]['training']['epochs']=[]
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6500111222267151})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5535382032394409})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5652501583099365})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6874510049819946})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6137709617614746})
store['active_learning_steps'][159]['training']['best_epoch']=2
store['active_learning_steps'][159]['evaluation_metrics']={'accuracy': 0.9059, 'crossentropy': 0.528536572265625}
store['active_learning_steps'][159]['acquisition']={'indices': [17759, 41384, 18147, 37437, 26573], 'labels': [-1, -1, -1, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][160]['training']={}
store['active_learning_steps'][160]['training']['epochs']=[]
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.700559139251709})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5856860876083374})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5730340480804443})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6342833042144775})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6562284231185913})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6383599042892456})
store['active_learning_steps'][160]['training']['best_epoch']=3
store['active_learning_steps'][160]['evaluation_metrics']={'accuracy': 0.9131, 'crossentropy': 0.50985859375}
store['active_learning_steps'][160]['acquisition']={'indices': [17547, 34219, 52611, 6717, 236], 'labels': [8, 3, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][161]['training']={}
store['active_learning_steps'][161]['training']['epochs']=[]
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6272598505020142})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4972323179244995})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4917859435081482})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6085093021392822})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5487903356552124})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5747568607330322})
store['active_learning_steps'][161]['training']['best_epoch']=3
store['active_learning_steps'][161]['evaluation_metrics']={'accuracy': 0.9162, 'crossentropy': 0.475415234375}
store['active_learning_steps'][161]['acquisition']={'indices': [751, 53654, 13334, 1322, 12543], 'labels': [5, 4, -1, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][162]['training']={}
store['active_learning_steps'][162]['training']['epochs']=[]
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6700105667114258})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5371456146240234})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4943048357963562})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5170497894287109})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5479813814163208})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.49696773290634155})
store['active_learning_steps'][162]['training']['best_epoch']=3
store['active_learning_steps'][162]['evaluation_metrics']={'accuracy': 0.9231, 'crossentropy': 0.468829296875}
store['active_learning_steps'][162]['acquisition']={'indices': [50817, 42002, 30051, 19406, 51260], 'labels': [-1, 1, 0, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][163]['training']={}
store['active_learning_steps'][163]['training']['epochs']=[]
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6556985378265381})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5681641101837158})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4692358076572418})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5591399669647217})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5010278820991516})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5962147116661072})
store['active_learning_steps'][163]['training']['best_epoch']=3
store['active_learning_steps'][163]['evaluation_metrics']={'accuracy': 0.9218, 'crossentropy': 0.44724833984375}
store['active_learning_steps'][163]['acquisition']={'indices': [36181, 49614, 24767, 44356, 31264], 'labels': [9, -1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][164]['training']={}
store['active_learning_steps'][164]['training']['epochs']=[]
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7183135151863098})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5888969898223877})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.46786731481552124})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6167768239974976})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5416151285171509})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5270935297012329})
store['active_learning_steps'][164]['training']['best_epoch']=3
store['active_learning_steps'][164]['evaluation_metrics']={'accuracy': 0.9271, 'crossentropy': 0.4311205078125}
store['active_learning_steps'][164]['acquisition']={'indices': [23537, 3745, 23217, 11769, 26342], 'labels': [8, -1, 9, 6, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][165]['training']={}
store['active_learning_steps'][165]['training']['epochs']=[]
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7174118757247925})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5626747608184814})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5288500785827637})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6017374992370605})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5128575563430786})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5803113579750061})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.669563889503479})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5989123582839966})
store['active_learning_steps'][165]['training']['best_epoch']=5
store['active_learning_steps'][165]['evaluation_metrics']={'accuracy': 0.9248, 'crossentropy': 0.467529638671875}
store['active_learning_steps'][165]['acquisition']={'indices': [9331, 55243, 4089, 36055, 18135], 'labels': [-1, -1, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][166]['training']={}
store['active_learning_steps'][166]['training']['epochs']=[]
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6493663191795349})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5268645286560059})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.46799755096435547})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5674498081207275})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.558250904083252})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6362200975418091})
store['active_learning_steps'][166]['training']['best_epoch']=3
store['active_learning_steps'][166]['evaluation_metrics']={'accuracy': 0.9283, 'crossentropy': 0.428550341796875}
store['active_learning_steps'][166]['acquisition']={'indices': [51027, 6436, 27088, 51998, 47809], 'labels': [5, 1, 4, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][167]['training']={}
store['active_learning_steps'][167]['training']['epochs']=[]
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6282224655151367})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5340864062309265})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5246325731277466})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5459141135215759})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5562655925750732})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5106505155563354})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5271023511886597})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5114209651947021})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6047390699386597})
store['active_learning_steps'][167]['training']['best_epoch']=6
store['active_learning_steps'][167]['evaluation_metrics']={'accuracy': 0.9304, 'crossentropy': 0.45845751953125}
store['active_learning_steps'][167]['acquisition']={'indices': [24196, 25708, 24217, 14843, 27220], 'labels': [-1, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][168]['training']={}
store['active_learning_steps'][168]['training']['epochs']=[]
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.655118465423584})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5369443297386169})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5222752094268799})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5492516756057739})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5511907339096069})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6068340539932251})
store['active_learning_steps'][168]['training']['best_epoch']=3
store['active_learning_steps'][168]['evaluation_metrics']={'accuracy': 0.9182, 'crossentropy': 0.474275830078125}
store['active_learning_steps'][168]['acquisition']={'indices': [15306, 8838, 26274, 55969, 23594], 'labels': [-1, -1, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][169]['training']={}
store['active_learning_steps'][169]['training']['epochs']=[]
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6736513376235962})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5276687145233154})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5193480849266052})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5255033373832703})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5746437311172485})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5447902679443359})
store['active_learning_steps'][169]['training']['best_epoch']=3
store['active_learning_steps'][169]['evaluation_metrics']={'accuracy': 0.9176, 'crossentropy': 0.455081396484375}
store['active_learning_steps'][169]['acquisition']={'indices': [10677, 9033, 3311, 28957, 41006], 'labels': [3, -1, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][170]['training']={}
store['active_learning_steps'][170]['training']['epochs']=[]
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6501858234405518})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5812468528747559})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.515030562877655})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5318669080734253})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5958921909332275})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5322527885437012})
store['active_learning_steps'][170]['training']['best_epoch']=3
store['active_learning_steps'][170]['evaluation_metrics']={'accuracy': 0.9111, 'crossentropy': 0.508656884765625}
store['active_learning_steps'][170]['acquisition']={'indices': [11072, 41213, 52430, 33056, 49903], 'labels': [-1, 6, -1, 6, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][171]['training']={}
store['active_learning_steps'][171]['training']['epochs']=[]
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6461662650108337})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5615816116333008})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5245621204376221})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.542892575263977})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5388643741607666})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5512580871582031})
store['active_learning_steps'][171]['training']['best_epoch']=3
store['active_learning_steps'][171]['evaluation_metrics']={'accuracy': 0.9129, 'crossentropy': 0.46661953125}
store['active_learning_steps'][171]['acquisition']={'indices': [7901, 25754, 39167, 22399, 42479], 'labels': [6, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][172]['training']={}
store['active_learning_steps'][172]['training']['epochs']=[]
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7232852578163147})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5512276887893677})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5252685546875})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5318589210510254})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5363904237747192})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.49221959710121155})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5128668546676636})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.591589093208313})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5543181896209717})
store['active_learning_steps'][172]['training']['best_epoch']=6
store['active_learning_steps'][172]['evaluation_metrics']={'accuracy': 0.9309, 'crossentropy': 0.47296376953125}
store['active_learning_steps'][172]['acquisition']={'indices': [19264, 54283, 58128, 29141, 55355], 'labels': [3, 5, 7, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][173]['training']={}
store['active_learning_steps'][173]['training']['epochs']=[]
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6263806223869324})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4770839810371399})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4514855742454529})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4903232455253601})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4587308168411255})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.47061359882354736})
store['active_learning_steps'][173]['training']['best_epoch']=3
store['active_learning_steps'][173]['evaluation_metrics']={'accuracy': 0.925, 'crossentropy': 0.422624951171875}
store['active_learning_steps'][173]['acquisition']={'indices': [45444, 38851, 21750, 55686, 20516], 'labels': [-1, -1, 2, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][174]['training']={}
store['active_learning_steps'][174]['training']['epochs']=[]
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6659280061721802})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.543627142906189})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5793641805648804})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5123164653778076})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5348537564277649})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5239996314048767})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6046586036682129})
store['active_learning_steps'][174]['training']['best_epoch']=4
store['active_learning_steps'][174]['evaluation_metrics']={'accuracy': 0.9229, 'crossentropy': 0.466641845703125}
store['active_learning_steps'][174]['acquisition']={'indices': [39722, 37736, 36390, 38246, 25995], 'labels': [-1, 4, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][175]['training']={}
store['active_learning_steps'][175]['training']['epochs']=[]
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6149968504905701})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5413454174995422})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.503510594367981})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.512783408164978})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5326807498931885})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5095841288566589})
store['active_learning_steps'][175]['training']['best_epoch']=3
store['active_learning_steps'][175]['evaluation_metrics']={'accuracy': 0.9225, 'crossentropy': 0.45087900390625}
store['active_learning_steps'][175]['acquisition']={'indices': [53013, 19308, 48677, 46205, 31788], 'labels': [-1, -1, 0, 6, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][176]['training']={}
store['active_learning_steps'][176]['training']['epochs']=[]
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6180458068847656})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5011372566223145})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5265246033668518})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6354767084121704})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5480146408081055})
store['active_learning_steps'][176]['training']['best_epoch']=2
store['active_learning_steps'][176]['evaluation_metrics']={'accuracy': 0.9163, 'crossentropy': 0.474071630859375}
