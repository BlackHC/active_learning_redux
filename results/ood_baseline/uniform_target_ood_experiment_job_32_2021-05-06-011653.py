store = {}
store['timestamp']=1620260213
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=32']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=32
store['worker_id']=32
store['num_workers']=40
store['config']={'seed': 44, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.403069496154785})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.7887887954711914})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.8772222995758057})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.008791923522949})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6582, 'crossentropy': 2.2032611328125}
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 19832], ['id', 26782], ['ood', 26401], ['id', 57501], ['id', 14018]], 'labels': [4, 2, 1, 8, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.5568757057189941})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.7595018148422241})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.9473159313201904})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.219724655151367})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7265, 'crossentropy': 1.45298125}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 9100], ['id', 30056], ['ood', 18143], ['id', 18796], ['ood', 4497]], 'labels': [4, 2, 3, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.3153231143951416})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.7627863883972168})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.05549693107605})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 2.2546346187591553})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7298, 'crossentropy': 1.3211412109375}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 37096], ['ood', 34523], ['id', 24195], ['id', 8834], ['ood', 757]], 'labels': [8, 6, 4, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.3277714252471924})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.5281667709350586})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.833967685699463})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.795536756515503})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7463, 'crossentropy': 1.2434794921875}
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 3996], ['id', 15633], ['id', 16688], ['ood', 17424], ['id', 38514]], 'labels': [1, 1, 8, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.545006275177002})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.672071099281311})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.7902711629867554})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.8105520009994507})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7503, 'crossentropy': 1.36370517578125}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 32905], ['ood', 48192], ['id', 56100], ['id', 47149], ['ood', 59189]], 'labels': [0, 8, 2, 7, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.264699935913086})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.4792925119400024})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.6677931547164917})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.9173176288604736})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7598, 'crossentropy': 1.211515234375}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 8318], ['id', 50688], ['id', 42044], ['id', 8505], ['id', 58780]], 'labels': [9, 3, 1, 3, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.1993310451507568})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.280346155166626})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.5120854377746582})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.5754444599151611})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7689, 'crossentropy': 1.1814623046875}
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 33072], ['id', 48405], ['id', 7974], ['id', 35280], ['id', 54331]], 'labels': [2, 4, 4, 6, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.0913357734680176})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.263547658920288})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.3074634075164795})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.395745038986206})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7932, 'crossentropy': 0.979754296875}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 3099], ['ood', 52447], ['id', 49271], ['ood', 23865], ['id', 51621]], 'labels': [9, 0, 4, 6, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.0823719501495361})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.0858829021453857})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.2357532978057861})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.3045482635498047})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7928, 'crossentropy': 1.00994140625}
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 56173], ['ood', 25709], ['id', 26932], ['id', 45051], ['id', 16900]], 'labels': [6, 1, 2, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9491543769836426})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.0556960105895996})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.1468055248260498})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.3094162940979004})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8128, 'crossentropy': 0.93544892578125}
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 50896], ['ood', 9557], ['ood', 4530], ['ood', 10857], ['ood', 52714]], 'labels': [6, 3, 8, 4, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.1666486263275146})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0297417640686035})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.2499300241470337})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.3529903888702393})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.3114690780639648})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.814, 'crossentropy': 1.0163982421875}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 15579], ['ood', 18571], ['id', 50750], ['id', 36348], ['ood', 58315]], 'labels': [5, 7, 0, 9, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 0.9634757041931152})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.0359073877334595})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.029191255569458})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.094611406326294})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7828, 'crossentropy': 0.96667470703125}
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 16152], ['id', 25168], ['id', 59430], ['ood', 48807], ['ood', 23746]], 'labels': [5, 9, 5, 5, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 0.9902338981628418})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9476555585861206})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.0491209030151367})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.0991615056991577})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.2132989168167114})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8123, 'crossentropy': 0.89456328125}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 30081], ['ood', 19963], ['id', 34860], ['id', 54724], ['id', 2576]], 'labels': [5, 6, 4, 3, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.8871681690216064})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9118227958679199})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9637437462806702})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.247262954711914})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8142, 'crossentropy': 0.85142900390625}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 30093], ['id', 49067], ['ood', 17197], ['ood', 57419], ['ood', 52309]], 'labels': [4, 2, 1, 5, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 0.962731122970581})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.9573796987533569})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.0219314098358154})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.0574668645858765})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.1501119136810303})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8208, 'crossentropy': 0.84832109375}
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 11569], ['ood', 19278], ['id', 31233], ['ood', 32798], ['ood', 52730]], 'labels': [8, 4, 2, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 0.9452210664749146})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.9232872128486633})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.011631965637207})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.054340124130249})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.1386336088180542})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8256, 'crossentropy': 0.81604658203125}
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 13268], ['ood', 49944], ['id', 21572], ['ood', 41175], ['ood', 48133]], 'labels': [2, 6, 7, 4, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.9077440500259399})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9172210693359375})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.887834906578064})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.040397047996521})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9951282739639282})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.0193538665771484})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.829, 'crossentropy': 0.817884375}
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 29107], ['ood', 44896], ['ood', 24020], ['ood', 46609], ['id', 45519]], 'labels': [1, 0, 2, 2, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.0106974840164185})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.9614020586013794})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.9373832941055298})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.990890622138977})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.1184639930725098})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.0439836978912354})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8279, 'crossentropy': 0.83401162109375}
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 18056], ['id', 51252], ['ood', 4158], ['id', 26155], ['ood', 4452]], 'labels': [9, 1, 6, 9, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 0.9612579941749573})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.8601492643356323})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.8323918581008911})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9447346925735474})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9541852474212646})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.070683479309082})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8462, 'crossentropy': 0.751918505859375}
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 37694], ['ood', 21908], ['ood', 5876], ['id', 42653], ['id', 31291]], 'labels': [8, 5, 4, 4, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 0.9580224752426147})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.8594454526901245})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9457840919494629})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9365147352218628})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.0113338232040405})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8339, 'crossentropy': 0.7678482421875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 34315], ['id', 50462], ['id', 30782], ['ood', 55266], ['id', 7561]], 'labels': [3, 9, 9, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9415931701660156})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.8798738718032837})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9671357870101929})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.0666571855545044})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.1639928817749023})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8263, 'crossentropy': 0.7992771484375}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 44257], ['ood', 29289], ['id', 13923], ['id', 41868], ['id', 32616]], 'labels': [7, 4, 1, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.877095103263855})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9030462503433228})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9573822617530823})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.0432490110397339})
store['active_learning_steps'][21]['training']['best_epoch']=1
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8303, 'crossentropy': 0.842741796875}
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 21167], ['ood', 33513], ['ood', 30349], ['ood', 58555], ['ood', 58251]], 'labels': [5, 7, 4, 7, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 0.9597519636154175})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.859612226486206})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9077253341674805})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.114089012145996})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9451916217803955})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8348, 'crossentropy': 0.78465048828125}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 20510], ['ood', 15487], ['id', 5116], ['id', 49161], ['ood', 23931]], 'labels': [0, 4, 8, 6, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8545318841934204})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.7881084084510803})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7614127397537231})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8523396253585815})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8587439060211182})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9277282953262329})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.856, 'crossentropy': 0.772559130859375}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 46643], ['ood', 38911], ['id', 8407], ['id', 31513], ['ood', 52707]], 'labels': [4, 5, 6, 2, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.8911169767379761})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8252456188201904})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7607277631759644})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.813291072845459})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7751075029373169})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9433703422546387})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8685, 'crossentropy': 0.70133642578125}
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 36583], ['ood', 58981], ['id', 4307], ['ood', 30795], ['id', 58908]], 'labels': [9, 7, 9, 0, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.901106595993042})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8177744150161743})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8268145322799683})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8971936702728271})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.946989893913269})
store['active_learning_steps'][25]['training']['best_epoch']=2
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8497, 'crossentropy': 0.761524365234375}
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 59356], ['ood', 5951], ['ood', 41124], ['id', 9327], ['id', 56270]], 'labels': [6, 5, 9, 7, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.905563235282898})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.7981892824172974})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8027820587158203})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8859527111053467})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8207893371582031})
store['active_learning_steps'][26]['training']['best_epoch']=2
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8543, 'crossentropy': 0.74211943359375}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 57527], ['id', 20716], ['id', 39632], ['ood', 24898], ['ood', 3636]], 'labels': [3, 5, 6, 8, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8623285293579102})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7469882965087891})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7697526216506958})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7824928760528564})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8565107583999634})
store['active_learning_steps'][27]['training']['best_epoch']=2
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8655, 'crossentropy': 0.67930625}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 33214], ['ood', 36866], ['ood', 2397], ['id', 7281], ['ood', 24652]], 'labels': [0, 6, 2, 0, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.8864507675170898})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7589133381843567})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8381177186965942})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7428762912750244})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7624133825302124})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7836207151412964})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8127878904342651})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8746, 'crossentropy': 0.670898779296875}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 29127], ['id', 18473], ['ood', 34863], ['id', 6279], ['ood', 18436]], 'labels': [7, 4, 6, 0, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8298935294151306})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7106049060821533})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7152048349380493})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8101010918617249})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7708518505096436})
store['active_learning_steps'][29]['training']['best_epoch']=2
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8604, 'crossentropy': 0.67176748046875}
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 27509], ['id', 2053], ['id', 16756], ['ood', 15771], ['ood', 54575]], 'labels': [3, 2, 7, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8536425232887268})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.7976751327514648})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.751572847366333})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8104234933853149})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7892526984214783})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.833740770816803})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8705, 'crossentropy': 0.70306728515625}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 12149], ['ood', 31103], ['ood', 36455], ['ood', 6664], ['ood', 29221]], 'labels': [7, 7, 0, 6, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.8789216876029968})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6943044662475586})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7431192398071289})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7054203748703003})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7120630741119385})
store['active_learning_steps'][31]['training']['best_epoch']=2
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8702, 'crossentropy': 0.659008642578125}
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 23496], ['id', 10450], ['ood', 31137], ['id', 35452], ['ood', 35032]], 'labels': [8, 3, 8, 6, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9235431551933289})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7505176067352295})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8778719902038574})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8218944072723389})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8189383745193481})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8652, 'crossentropy': 0.70407060546875}
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 36773], ['ood', 1902], ['id', 1148], ['ood', 27185], ['id', 19734]], 'labels': [3, 3, 1, 3, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.8760913610458374})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7990217208862305})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8029370903968811})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7198630571365356})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7756409049034119})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8943819999694824})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8466899394989014})
store['active_learning_steps'][33]['training']['best_epoch']=4
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8661, 'crossentropy': 0.729178369140625}
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 18281], ['ood', 19510], ['id', 50463], ['id', 36388], ['ood', 19768]], 'labels': [1, 6, 0, 1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.8990902900695801})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7349667549133301})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7810800075531006})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8000837564468384})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8109958171844482})
store['active_learning_steps'][34]['training']['best_epoch']=2
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8491, 'crossentropy': 0.723663427734375}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 2622], ['ood', 49835], ['id', 9909], ['id', 34686], ['ood', 839]], 'labels': [5, 1, 6, 6, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.830902099609375})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.765134871006012})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7508007287979126})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7437966465950012})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.749422550201416})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7705538272857666})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8249803185462952})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.872, 'crossentropy': 0.67048916015625}
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 17275], ['ood', 26464], ['id', 50408], ['ood', 43590], ['id', 20234]], 'labels': [8, 9, 9, 6, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8600754737854004})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7154237031936646})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7023611068725586})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7685451507568359})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7717685699462891})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8397184610366821})
store['active_learning_steps'][36]['training']['best_epoch']=3
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8646, 'crossentropy': 0.663229931640625}
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 11556], ['id', 53879], ['ood', 5731], ['ood', 8270], ['id', 18345]], 'labels': [9, 2, 9, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.931774914264679})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6959760189056396})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6797505617141724})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7087467908859253})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8090304732322693})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8000384569168091})
store['active_learning_steps'][37]['training']['best_epoch']=3
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8765, 'crossentropy': 0.651040869140625}
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 30324], ['ood', 2333], ['id', 20030], ['id', 33108], ['ood', 56682]], 'labels': [2, 4, 7, 1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8662266731262207})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7400079965591431})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.658153235912323})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7781323194503784})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.727920651435852})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7424783110618591})
store['active_learning_steps'][38]['training']['best_epoch']=3
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8817, 'crossentropy': 0.597661181640625}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 11246], ['ood', 53075], ['id', 57064], ['ood', 10034], ['ood', 15276]], 'labels': [9, 4, 0, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8060258626937866})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6635497808456421})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7297821044921875})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7731024026870728})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7351601719856262})
store['active_learning_steps'][39]['training']['best_epoch']=2
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8724, 'crossentropy': 0.621512548828125}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 52585], ['ood', 37994], ['ood', 44801], ['ood', 19532], ['ood', 50125]], 'labels': [3, 3, 8, 0, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.915742039680481})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7786812782287598})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7000238299369812})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7474980354309082})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7811616659164429})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8216646909713745})
store['active_learning_steps'][40]['training']['best_epoch']=3
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8738, 'crossentropy': 0.638605712890625}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 873], ['ood', 35284], ['id', 16281], ['ood', 29554], ['id', 19778]], 'labels': [2, 8, 2, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.9002847075462341})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7368066310882568})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7073982954025269})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7253611087799072})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7840631008148193})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9523341059684753})
store['active_learning_steps'][41]['training']['best_epoch']=3
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8704, 'crossentropy': 0.67474912109375}
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 47461], ['ood', 4467], ['id', 7337], ['ood', 11521], ['ood', 47687]], 'labels': [6, 4, 2, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9371361136436462})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7075515389442444})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.776008129119873})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7743978500366211})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8147105574607849})
store['active_learning_steps'][42]['training']['best_epoch']=2
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8719, 'crossentropy': 0.67787177734375}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 17486], ['id', 12866], ['id', 21068], ['ood', 32691], ['id', 33623]], 'labels': [7, 6, 1, 5, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8555158376693726})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7682756185531616})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7325177192687988})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.691963791847229})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7795842885971069})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7555528879165649})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.811992883682251})
store['active_learning_steps'][43]['training']['best_epoch']=4
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8878, 'crossentropy': 0.634981103515625}
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 32472], ['ood', 52481], ['id', 29810], ['id', 8987], ['ood', 14603]], 'labels': [1, 5, 1, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.8923377394676208})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7231361865997314})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.71943199634552})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7437912225723267})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8339922428131104})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8609037399291992})
store['active_learning_steps'][44]['training']['best_epoch']=3
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8812, 'crossentropy': 0.631358447265625}
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 11033], ['ood', 54708], ['ood', 14087], ['ood', 44689], ['id', 35433]], 'labels': [2, 8, 5, 0, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.8957887887954712})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6971830129623413})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7034986019134521})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7334620952606201})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7262412309646606})
store['active_learning_steps'][45]['training']['best_epoch']=2
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8747, 'crossentropy': 0.6331841796875}
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 32103], ['id', 16975], ['id', 1215], ['id', 42943], ['id', 52302]], 'labels': [8, 0, 4, 9, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.9314990639686584})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6971902847290039})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6995292901992798})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7821446061134338})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7391881942749023})
store['active_learning_steps'][46]['training']['best_epoch']=2
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8726, 'crossentropy': 0.660268115234375}
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 49352], ['ood', 45562], ['ood', 54099], ['id', 42032], ['id', 49202]], 'labels': [7, 8, 5, 4, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.859355092048645})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6715571880340576})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7238554954528809})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7140810489654541})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7622238397598267})
store['active_learning_steps'][47]['training']['best_epoch']=2
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8681, 'crossentropy': 0.647547021484375}
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 318], ['id', 281], ['id', 49577], ['ood', 23137], ['ood', 32244]], 'labels': [2, 3, 6, 8, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.8601078987121582})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.661754846572876})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.675299882888794})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7100746035575867})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7196018695831299})
store['active_learning_steps'][48]['training']['best_epoch']=2
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8824, 'crossentropy': 0.586476708984375}
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 12842], ['id', 52297], ['id', 1462], ['ood', 32509], ['id', 44043]], 'labels': [1, 6, 9, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7898514270782471})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7025991082191467})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7015936374664307})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6819945573806763})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7869249582290649})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8820395469665527})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7757343053817749})
store['active_learning_steps'][49]['training']['best_epoch']=4
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8828, 'crossentropy': 0.66164482421875}
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 40960], ['id', 23661], ['ood', 14012], ['id', 51241], ['id', 48536]], 'labels': [4, 7, 0, 2, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8662893772125244})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7106898427009583})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6961758136749268})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.711753785610199})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7848294973373413})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8322724103927612})
store['active_learning_steps'][50]['training']['best_epoch']=3
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.877, 'crossentropy': 0.62155517578125}
store['active_learning_steps'][50]['acquisition']={'indices': [['ood', 44458], ['id', 21586], ['id', 19141], ['id', 5685], ['ood', 22612]], 'labels': [6, 0, 7, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 0.9046344757080078})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7218409776687622})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6668601036071777})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7574803829193115})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7701215744018555})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7527560591697693})
store['active_learning_steps'][51]['training']['best_epoch']=3
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8748, 'crossentropy': 0.646817919921875}
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 27576], ['ood', 23764], ['ood', 6640], ['id', 26834], ['ood', 55718]], 'labels': [3, 2, 3, 9, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 0.9146733283996582})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7020763158798218})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6531598567962646})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6895363330841064})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7134976387023926})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7620483040809631})
store['active_learning_steps'][52]['training']['best_epoch']=3
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.8848, 'crossentropy': 0.626316064453125}
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 48283], ['ood', 30859], ['id', 16273], ['id', 18294], ['id', 15207]], 'labels': [4, 5, 6, 4, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.90314781665802})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7307654619216919})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7198895215988159})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7348788380622864})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6588869094848633})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8501060009002686})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7718095779418945})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.749243974685669})
store['active_learning_steps'][53]['training']['best_epoch']=5
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8948, 'crossentropy': 0.61690478515625}
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 24196], ['ood', 46959], ['ood', 5758], ['id', 26443], ['ood', 56011]], 'labels': [5, 2, 0, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.7939789295196533})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6705156564712524})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6526179313659668})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6987114548683167})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.703887403011322})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7078723907470703})
store['active_learning_steps'][54]['training']['best_epoch']=3
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8881, 'crossentropy': 0.588392578125}
store['active_learning_steps'][54]['acquisition']={'indices': [['ood', 17711], ['id', 56933], ['id', 44096], ['id', 1903], ['id', 8564]], 'labels': [1, 9, 0, 9, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8531118035316467})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6377636194229126})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6364505887031555})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6573399305343628})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6612005233764648})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6655364036560059})
store['active_learning_steps'][55]['training']['best_epoch']=3
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.8935, 'crossentropy': 0.569581201171875}
store['active_learning_steps'][55]['acquisition']={'indices': [['ood', 39602], ['id', 26192], ['ood', 31934], ['id', 23309], ['ood', 12239]], 'labels': [1, 4, 2, 7, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8332648277282715})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7051844596862793})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7123134732246399})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7543826699256897})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7717060446739197})
store['active_learning_steps'][56]['training']['best_epoch']=2
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8786, 'crossentropy': 0.635484423828125}
store['active_learning_steps'][56]['acquisition']={'indices': [['ood', 32393], ['id', 58170], ['id', 6970], ['id', 56742], ['id', 44497]], 'labels': [8, 0, 0, 9, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.8656841516494751})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6564664840698242})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7012577056884766})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7291445732116699})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6884335279464722})
store['active_learning_steps'][57]['training']['best_epoch']=2
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8899, 'crossentropy': 0.577584716796875}
store['active_learning_steps'][57]['acquisition']={'indices': [['ood', 4885], ['id', 39083], ['ood', 15422], ['ood', 41661], ['id', 12784]], 'labels': [9, 4, 5, 0, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.84031081199646})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6517441272735596})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.679015040397644})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7067428827285767})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6514556407928467})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7738760709762573})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7334747314453125})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.763323187828064})
store['active_learning_steps'][58]['training']['best_epoch']=5
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9055, 'crossentropy': 0.56068701171875}
store['active_learning_steps'][58]['acquisition']={'indices': [['id', 10815], ['ood', 8924], ['id', 34827], ['ood', 37336], ['id', 49986]], 'labels': [7, 0, 6, 4, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8613837361335754})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7029705047607422})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.679699182510376})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7212918996810913})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6806514859199524})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.748746931552887})
store['active_learning_steps'][59]['training']['best_epoch']=3
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.8907, 'crossentropy': 0.61509775390625}
store['active_learning_steps'][59]['acquisition']={'indices': [['ood', 54247], ['ood', 12727], ['ood', 27131], ['id', 26768], ['ood', 9908]], 'labels': [4, 3, 9, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.9359342455863953})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.659791886806488})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7236720323562622})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6777315139770508})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6932590007781982})
store['active_learning_steps'][60]['training']['best_epoch']=2
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8857, 'crossentropy': 0.61953271484375}
store['active_learning_steps'][60]['acquisition']={'indices': [['ood', 24501], ['id', 5248], ['id', 35211], ['ood', 25928], ['ood', 30964]], 'labels': [9, 8, 6, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.885851263999939})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6534342765808105})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6841627359390259})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7057344317436218})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6804424524307251})
store['active_learning_steps'][61]['training']['best_epoch']=2
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.8847, 'crossentropy': 0.58684326171875}
store['active_learning_steps'][61]['acquisition']={'indices': [['ood', 49795], ['ood', 27270], ['ood', 21422], ['ood', 13313], ['ood', 56321]], 'labels': [3, 2, 9, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8872808218002319})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7116538882255554})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6747334003448486})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6536729335784912})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7191132307052612})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7474303245544434})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7072545289993286})
store['active_learning_steps'][62]['training']['best_epoch']=4
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.8858, 'crossentropy': 0.603283056640625}
store['active_learning_steps'][62]['acquisition']={'indices': [['id', 59463], ['ood', 12231], ['ood', 25654], ['ood', 20919], ['id', 25882]], 'labels': [6, 6, 9, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.9086796045303345})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6498340368270874})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6549080014228821})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7647310495376587})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7324974536895752})
store['active_learning_steps'][63]['training']['best_epoch']=2
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.8834, 'crossentropy': 0.59863251953125}
store['active_learning_steps'][63]['acquisition']={'indices': [['id', 35330], ['ood', 44214], ['ood', 19353], ['id', 42286], ['ood', 34428]], 'labels': [9, 7, 7, 4, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8510335683822632})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6577974557876587})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6060237884521484})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6328009963035583})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6408822536468506})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6759835481643677})
store['active_learning_steps'][64]['training']['best_epoch']=3
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9019, 'crossentropy': 0.552288330078125}
store['active_learning_steps'][64]['acquisition']={'indices': [['ood', 29361], ['ood', 20599], ['ood', 26013], ['id', 1244], ['id', 11753]], 'labels': [9, 9, 8, 3, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9095958471298218})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6882957816123962})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6273062229156494})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6631739139556885})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.624605655670166})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7139731049537659})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7787725925445557})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6860432624816895})
store['active_learning_steps'][65]['training']['best_epoch']=5
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9112, 'crossentropy': 0.541974365234375}
store['active_learning_steps'][65]['acquisition']={'indices': [['ood', 22356], ['id', 53768], ['ood', 29518], ['ood', 28917], ['id', 55159]], 'labels': [5, 4, 6, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.8971775770187378})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6569689512252808})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6181484460830688})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6714569330215454})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6345000267028809})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6289613842964172})
store['active_learning_steps'][66]['training']['best_epoch']=3
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.8989, 'crossentropy': 0.540289990234375}
store['active_learning_steps'][66]['acquisition']={'indices': [['ood', 54176], ['id', 52016], ['ood', 42679], ['ood', 24869], ['id', 36450]], 'labels': [4, 2, 5, 0, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8533647656440735})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6939520835876465})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6549372673034668})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6593062877655029})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6582056879997253})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7108249068260193})
store['active_learning_steps'][67]['training']['best_epoch']=3
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.8984, 'crossentropy': 0.5961638671875}
store['active_learning_steps'][67]['acquisition']={'indices': [['id', 56142], ['id', 6506], ['ood', 13401], ['id', 11237], ['ood', 58826]], 'labels': [4, 8, 6, 5, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8672196269035339})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.638979971408844})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6101226806640625})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6094964742660522})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6323214769363403})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7028149366378784})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6137303113937378})
store['active_learning_steps'][68]['training']['best_epoch']=4
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9155, 'crossentropy': 0.515058935546875}
store['active_learning_steps'][68]['acquisition']={'indices': [['id', 20452], ['ood', 38233], ['ood', 38649], ['id', 12626], ['ood', 5327]], 'labels': [7, 7, 8, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9419443607330322})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6712815761566162})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7017693519592285})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.652259886264801})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6766373515129089})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6528139114379883})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.656668484210968})
store['active_learning_steps'][69]['training']['best_epoch']=4
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9036, 'crossentropy': 0.563815625}
store['active_learning_steps'][69]['acquisition']={'indices': [['id', 51293], ['id', 59803], ['id', 34109], ['ood', 47191], ['id', 33281]], 'labels': [6, 8, 4, 4, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.9803775548934937})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7069917321205139})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.669975757598877})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7879757881164551})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6545941829681396})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6555854082107544})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6821104884147644})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7040438055992126})
store['active_learning_steps'][70]['training']['best_epoch']=5
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9091, 'crossentropy': 0.552683837890625}
store['active_learning_steps'][70]['acquisition']={'indices': [['ood', 31132], ['ood', 33329], ['ood', 23698], ['id', 54440], ['id', 55606]], 'labels': [3, 1, 4, 2, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8614469766616821})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.6976169347763062})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6261655688285828})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6366295218467712})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6380982398986816})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6519026160240173})
store['active_learning_steps'][71]['training']['best_epoch']=3
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9035, 'crossentropy': 0.528033984375}
store['active_learning_steps'][71]['acquisition']={'indices': [['id', 56693], ['ood', 57572], ['id', 34537], ['ood', 15676], ['ood', 6775]], 'labels': [6, 4, 4, 9, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8273578882217407})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6304718852043152})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6510117053985596})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6040569543838501})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.647186279296875})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6221145391464233})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6143560409545898})
store['active_learning_steps'][72]['training']['best_epoch']=4
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.915, 'crossentropy': 0.491673876953125}
store['active_learning_steps'][72]['acquisition']={'indices': [['ood', 2395], ['id', 26840], ['ood', 32143], ['id', 21575], ['ood', 20535]], 'labels': [4, 0, 0, 1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9770848751068115})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6361751556396484})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5613083839416504})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6211012005805969})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6203087568283081})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6334731578826904})
store['active_learning_steps'][73]['training']['best_epoch']=3
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9107, 'crossentropy': 0.510448193359375}
store['active_learning_steps'][73]['acquisition']={'indices': [['ood', 45816], ['id', 12546], ['ood', 9689], ['ood', 51317], ['id', 23594]], 'labels': [9, 3, 8, 0, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9126351475715637})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6370244026184082})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6557359099388123})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6143923997879028})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6712250113487244})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6385000944137573})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6585792303085327})
store['active_learning_steps'][74]['training']['best_epoch']=4
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9057, 'crossentropy': 0.53683994140625}
store['active_learning_steps'][74]['acquisition']={'indices': [['id', 26272], ['id', 42641], ['id', 734], ['id', 30343], ['ood', 10064]], 'labels': [7, 5, 8, 6, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8493534326553345})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7059938907623291})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6746779680252075})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6571242809295654})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6189830303192139})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6550288796424866})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7083044052124023})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6433473825454712})
store['active_learning_steps'][75]['training']['best_epoch']=5
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.914, 'crossentropy': 0.503899609375}
store['active_learning_steps'][75]['acquisition']={'indices': [['id', 2610], ['ood', 23903], ['id', 29640], ['id', 17137], ['ood', 54997]], 'labels': [8, 0, 2, 2, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7745545506477356})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6339080929756165})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5938190221786499})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6434984803199768})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6593163013458252})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6655192375183105})
store['active_learning_steps'][76]['training']['best_epoch']=3
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9051, 'crossentropy': 0.5262330078125}
store['active_learning_steps'][76]['acquisition']={'indices': [['ood', 36526], ['id', 25454], ['id', 31604], ['ood', 2855], ['id', 40307]], 'labels': [6, 3, 0, 6, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8673018217086792})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6883641481399536})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6629112958908081})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.632203221321106})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7100905179977417})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6858854293823242})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.64776611328125})
store['active_learning_steps'][77]['training']['best_epoch']=4
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9109, 'crossentropy': 0.53150771484375}
store['active_learning_steps'][77]['acquisition']={'indices': [['ood', 4212], ['id', 52151], ['ood', 27851], ['id', 41427], ['ood', 37791]], 'labels': [9, 9, 4, 2, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9192798733711243})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6759259700775146})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6701256036758423})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6432451605796814})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6599842309951782})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6569679379463196})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6167482733726501})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6929046511650085})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7274411916732788})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7049236297607422})
store['active_learning_steps'][78]['training']['best_epoch']=7
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9177, 'crossentropy': 0.50993046875}
store['active_learning_steps'][78]['acquisition']={'indices': [['ood', 8006], ['id', 38362], ['id', 22945], ['id', 30342], ['ood', 29824]], 'labels': [2, 5, 2, 9, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8711526393890381})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6615936756134033})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5784595012664795})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5531509518623352})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6025450825691223})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6790047883987427})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6510677337646484})
store['active_learning_steps'][79]['training']['best_epoch']=4
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9132, 'crossentropy': 0.4920169921875}
store['active_learning_steps'][79]['acquisition']={'indices': [['ood', 58840], ['ood', 42480], ['ood', 32349], ['ood', 12435], ['ood', 11812]], 'labels': [5, 2, 6, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8491683006286621})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6026526689529419})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6044042110443115})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.607401967048645})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6370147466659546})
store['active_learning_steps'][80]['training']['best_epoch']=2
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.8993, 'crossentropy': 0.545770751953125}
store['active_learning_steps'][80]['acquisition']={'indices': [['ood', 58295], ['ood', 58061], ['ood', 33106], ['ood', 52317], ['id', 18681]], 'labels': [3, 9, 6, 3, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8355900049209595})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6799695491790771})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6340638399124146})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6633637547492981})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.649788498878479})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6838669180870056})
store['active_learning_steps'][81]['training']['best_epoch']=3
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9055, 'crossentropy': 0.5138111328125}
store['active_learning_steps'][81]['acquisition']={'indices': [['id', 50420], ['id', 10531], ['ood', 19743], ['id', 8320], ['id', 51134]], 'labels': [5, 0, 1, 5, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8716024160385132})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6220373511314392})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6444805264472961})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6579818725585938})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6325628757476807})
store['active_learning_steps'][82]['training']['best_epoch']=2
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9054, 'crossentropy': 0.54216533203125}
store['active_learning_steps'][82]['acquisition']={'indices': [['id', 2187], ['id', 30713], ['ood', 14330], ['ood', 812], ['ood', 58739]], 'labels': [7, 7, 4, 0, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.8677427768707275})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6363667249679565})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6442203521728516})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6191240549087524})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.643960177898407})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6802392601966858})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6568659543991089})
store['active_learning_steps'][83]['training']['best_epoch']=4
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9098, 'crossentropy': 0.510893994140625}
store['active_learning_steps'][83]['acquisition']={'indices': [['id', 57499], ['ood', 49902], ['ood', 43989], ['id', 14422], ['ood', 41736]], 'labels': [4, 8, 1, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.799490213394165})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6490347385406494})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.613614559173584})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6258470416069031})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6474783420562744})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6911213397979736})
store['active_learning_steps'][84]['training']['best_epoch']=3
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9088, 'crossentropy': 0.521140869140625}
store['active_learning_steps'][84]['acquisition']={'indices': [['ood', 16600], ['ood', 18255], ['ood', 42532], ['id', 56896], ['id', 8483]], 'labels': [0, 8, 6, 9, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7917203903198242})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.571391224861145})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5760873556137085})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5944588780403137})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5757550001144409})
store['active_learning_steps'][85]['training']['best_epoch']=2
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9086, 'crossentropy': 0.529674755859375}
store['active_learning_steps'][85]['acquisition']={'indices': [['id', 51939], ['id', 42529], ['id', 58777], ['ood', 43130], ['id', 34852]], 'labels': [4, 9, 8, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9046896696090698})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6664180755615234})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5948200225830078})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6421523094177246})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6214618682861328})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6558442115783691})
store['active_learning_steps'][86]['training']['best_epoch']=3
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9032, 'crossentropy': 0.540775830078125}
