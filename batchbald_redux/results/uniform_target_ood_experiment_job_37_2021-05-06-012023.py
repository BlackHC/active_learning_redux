store = {}
store['timestamp']=1620260423
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=37']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=37
store['worker_id']=37
store['num_workers']=40
store['config']={'seed': 54, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.230677366256714})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.6202774047851562})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.7755603790283203})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.4874346256256104})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6887, 'crossentropy': 1.98304765625}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 42162], ['id', 11096], ['id', 37171], ['id', 7815], ['id', 43407]], 'labels': [6, 9, 4, 6, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.012529134750366})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.348221778869629})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.4046506881713867})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.8628792762756348})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.704, 'crossentropy': 1.811687109375}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 57506], ['id', 36674], ['id', 55849], ['id', 13502], ['id', 14680]], 'labels': [2, 4, 9, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.9001739025115967})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.1621620655059814})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.5033116340637207})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.3671956062316895})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7268, 'crossentropy': 1.61524404296875}
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 33523], ['id', 1833], ['id', 13296], ['id', 43002], ['id', 4952]], 'labels': [9, 7, 1, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.601440668106079})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.962449312210083})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.060680389404297})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.288463830947876})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7308, 'crossentropy': 1.44314033203125}
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 31530], ['ood', 45099], ['ood', 34421], ['ood', 30589], ['ood', 8749]], 'labels': [7, 8, 6, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.320671558380127})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.441711664199829})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.536153793334961})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.6324167251586914})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7431, 'crossentropy': 1.20222734375}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 21679], ['ood', 4605], ['id', 20965], ['id', 2439], ['ood', 34925]], 'labels': [7, 9, 3, 4, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.2834969758987427})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.4411870241165161})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.4872384071350098})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.7205581665039062})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7446, 'crossentropy': 1.163844921875}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 39201], ['ood', 29669], ['ood', 44737], ['ood', 6768], ['id', 15997]], 'labels': [8, 1, 1, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.1610151529312134})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.2999591827392578})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.3096637725830078})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.4763853549957275})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7764, 'crossentropy': 1.0277966796875}
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 24499], ['id', 17832], ['id', 30272], ['ood', 35323], ['ood', 48288]], 'labels': [2, 3, 4, 3, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.059306263923645})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.106353521347046})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.279759407043457})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.4195876121520996})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7761, 'crossentropy': 0.98045634765625}
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 55249], ['id', 6514], ['id', 50923], ['id', 38810], ['id', 51683]], 'labels': [2, 9, 7, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.0213985443115234})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.199053168296814})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.247865915298462})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.3468959331512451})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.791, 'crossentropy': 0.9700673828125}
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 50630], ['ood', 32770], ['id', 487], ['id', 37163], ['id', 46691]], 'labels': [8, 6, 9, 3, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.0544761419296265})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.0506649017333984})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.0510852336883545})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.2276626825332642})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.3608672618865967})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7988, 'crossentropy': 0.99959287109375}
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 17743], ['ood', 23941], ['ood', 57264], ['id', 14020], ['ood', 52183]], 'labels': [4, 8, 4, 8, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.0274596214294434})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.053032398223877})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.1981923580169678})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.1339068412780762})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.779, 'crossentropy': 0.99612236328125}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 37042], ['id', 52213], ['id', 18259], ['ood', 4384], ['ood', 11028]], 'labels': [3, 5, 1, 4, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.0255928039550781})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9706982374191284})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.049564003944397})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.080869197845459})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.1569790840148926})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8006, 'crossentropy': 0.93893935546875}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 38287], ['id', 26766], ['ood', 20739], ['id', 34914], ['ood', 18914]], 'labels': [5, 6, 2, 7, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.027074933052063})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.1105903387069702})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.1705212593078613})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.2485864162445068})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7869, 'crossentropy': 0.96593359375}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 38556], ['ood', 19743], ['id', 46053], ['id', 43627], ['id', 19335]], 'labels': [7, 1, 7, 7, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.0613439083099365})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.0887095928192139})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.2218575477600098})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.1359450817108154})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.7829, 'crossentropy': 0.9836123046875}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 56846], ['id', 29935], ['ood', 18756], ['id', 4265], ['ood', 28255]], 'labels': [7, 9, 9, 0, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.0186195373535156})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.0905355215072632})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.1820237636566162})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.1974202394485474})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7777, 'crossentropy': 1.0109681640625}
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 5053], ['ood', 26536], ['id', 39164], ['id', 23770], ['id', 45646]], 'labels': [3, 4, 6, 2, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 0.904629647731781})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9668759107589722})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.05220365524292})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.040112853050232})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.7955, 'crossentropy': 0.89909775390625}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 53911], ['ood', 33665], ['id', 6763], ['ood', 36909], ['ood', 57608]], 'labels': [7, 1, 0, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.9387560486793518})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9010652899742126})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9521188139915466})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.0362635850906372})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.973371148109436})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8268, 'crossentropy': 0.83909384765625}
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 47288], ['id', 22939], ['id', 44183], ['id', 22051], ['ood', 52526]], 'labels': [8, 6, 1, 4, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.9103138446807861})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9059019684791565})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.890434741973877})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9194098114967346})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9404822587966919})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9603203535079956})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8383, 'crossentropy': 0.85105986328125}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 2798], ['ood', 49926], ['id', 59031], ['ood', 51047], ['ood', 44100]], 'labels': [9, 2, 7, 7, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9388285875320435})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8093754649162292})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9033195972442627})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9413254261016846})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9843136072158813})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8465, 'crossentropy': 0.76388837890625}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 26793], ['id', 51638], ['id', 58684], ['ood', 40798], ['id', 5444]], 'labels': [5, 0, 4, 0, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.8951272964477539})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8543385863304138})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9653501510620117})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9849656820297241})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0474276542663574})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8421, 'crossentropy': 0.80440791015625}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 47597], ['ood', 19665], ['ood', 23954], ['id', 56970], ['ood', 34150]], 'labels': [8, 1, 2, 4, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9702857732772827})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8635672330856323})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9902551174163818})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9896398186683655})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0279051065444946})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8297, 'crossentropy': 0.8469888671875}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 16270], ['id', 14029], ['id', 37242], ['ood', 26065], ['id', 2229]], 'labels': [9, 5, 9, 9, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.896277666091919})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8481911420822144})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8367726802825928})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9003099203109741})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8428059816360474})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.945710301399231})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.856, 'crossentropy': 0.7804603515625}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 38891], ['id', 21291], ['ood', 8889], ['id', 8605], ['ood', 14522]], 'labels': [4, 6, 9, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9243752360343933})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.876755952835083})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9301304817199707})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9521054029464722})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9034987688064575})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8418, 'crossentropy': 0.8220466796875}
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 18646], ['ood', 17559], ['ood', 56731], ['id', 54825], ['id', 15740]], 'labels': [2, 9, 1, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8476693630218506})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8320984840393066})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8240219354629517})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8869526386260986})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9555412530899048})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9611010551452637})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8479, 'crossentropy': 0.83220654296875}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 43661], ['ood', 58753], ['ood', 39585], ['id', 42321], ['ood', 57661]], 'labels': [9, 9, 3, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.8777068853378296})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8469313979148865})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7594178915023804})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8682466745376587})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.0133451223373413})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8958324193954468})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8576, 'crossentropy': 0.745693603515625}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 7713], ['id', 20496], ['ood', 42522], ['id', 50149], ['ood', 54161]], 'labels': [9, 4, 5, 4, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.9585925340652466})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8117691278457642})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8349703550338745})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8919440507888794})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9695663452148438})
store['active_learning_steps'][25]['training']['best_epoch']=2
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8348, 'crossentropy': 0.7955818359375}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 54163], ['id', 44507], ['id', 4060], ['ood', 57201], ['id', 6409]], 'labels': [8, 8, 9, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8170689344406128})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8759380578994751})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8662343621253967})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8908238410949707})
store['active_learning_steps'][26]['training']['best_epoch']=1
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8362, 'crossentropy': 0.80365751953125}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 37437], ['id', 39379], ['ood', 4099], ['ood', 3097], ['ood', 51279]], 'labels': [2, 6, 3, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8198059797286987})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7835120558738708})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6806862354278564})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7671287059783936})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8897264003753662})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8038601875305176})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8725, 'crossentropy': 0.67893837890625}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 4326], ['id', 41775], ['id', 15399], ['id', 26804], ['ood', 46199]], 'labels': [7, 4, 0, 8, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8400923013687134})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7254704236984253})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7197568416595459})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7472615242004395})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7700729966163635})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8190800547599792})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8856, 'crossentropy': 0.665793310546875}
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 54015], ['id', 54137], ['id', 6986], ['ood', 8087], ['ood', 33976]], 'labels': [3, 8, 7, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7925432920455933})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8061513900756836})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7307608127593994})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.710819661617279})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.781804084777832})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7454308271408081})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8618115186691284})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.886, 'crossentropy': 0.726778173828125}
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 28539], ['id', 16907], ['id', 1271], ['ood', 52071], ['id', 43190]], 'labels': [8, 1, 4, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8388059139251709})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7181464433670044})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7806509137153625})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7325594425201416})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7747238874435425})
store['active_learning_steps'][30]['training']['best_epoch']=2
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8692, 'crossentropy': 0.69130751953125}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 53843], ['id', 12845], ['id', 25115], ['id', 45768], ['ood', 8931]], 'labels': [7, 1, 7, 1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.81529700756073})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6876838803291321})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6911823749542236})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7394803762435913})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7181966304779053})
store['active_learning_steps'][31]['training']['best_epoch']=2
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.877, 'crossentropy': 0.678634814453125}
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 38362], ['ood', 51092], ['id', 3955], ['id', 36532], ['id', 5586]], 'labels': [2, 7, 1, 1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.8838838338851929})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7935041189193726})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8393723368644714})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8438222408294678})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9132670164108276})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8639, 'crossentropy': 0.75723818359375}
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 24046], ['ood', 11194], ['id', 33592], ['id', 6207], ['id', 59900]], 'labels': [4, 2, 9, 0, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8924472332000732})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7751805782318115})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.807968258857727})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7986619472503662})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7693963646888733})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8246186971664429})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9010261297225952})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9002733826637268})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8819, 'crossentropy': 0.737817333984375}
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 12072], ['id', 16090], ['id', 58918], ['id', 37254], ['id', 43101]], 'labels': [4, 9, 9, 6, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8694192171096802})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7317030429840088})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7388278245925903})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7472306489944458})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7281444668769836})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7838886976242065})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7887005805969238})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8505624532699585})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8766, 'crossentropy': 0.70008681640625}
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 2317], ['ood', 19349], ['ood', 34070], ['ood', 33646], ['id', 29842]], 'labels': [7, 1, 4, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8145540356636047})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6861851215362549})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7297900915145874})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7564612627029419})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.815717339515686})
store['active_learning_steps'][35]['training']['best_epoch']=2
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.872, 'crossentropy': 0.685054052734375}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 9546], ['ood', 12491], ['ood', 55463], ['id', 5935], ['id', 12789]], 'labels': [2, 4, 7, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8670827746391296})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.726667046546936})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7478736042976379})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.806930661201477})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8396029472351074})
store['active_learning_steps'][36]['training']['best_epoch']=2
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8768, 'crossentropy': 0.652089013671875}
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 37752], ['ood', 42291], ['ood', 9813], ['ood', 55101], ['id', 5497]], 'labels': [7, 2, 9, 5, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8780391812324524})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.719295084476471})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7104642391204834})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6979646682739258})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7987000942230225})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.710504412651062})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7881935834884644})
store['active_learning_steps'][37]['training']['best_epoch']=4
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8832, 'crossentropy': 0.6858046875}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 37575], ['id', 32707], ['ood', 23946], ['ood', 37642], ['ood', 17652]], 'labels': [9, 5, 1, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8841843008995056})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7052491307258606})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7176626920700073})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6608407497406006})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.83402419090271})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7915636897087097})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7784016728401184})
store['active_learning_steps'][38]['training']['best_epoch']=4
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8912, 'crossentropy': 0.62715087890625}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 27415], ['ood', 54705], ['ood', 4652], ['ood', 49589], ['id', 5853]], 'labels': [6, 3, 3, 3, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7941267490386963})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6562099456787109})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6636627912521362})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6879652738571167})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6910699605941772})
store['active_learning_steps'][39]['training']['best_epoch']=2
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8861, 'crossentropy': 0.58918115234375}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 50023], ['ood', 24145], ['id', 10764], ['ood', 51494], ['id', 24828]], 'labels': [1, 8, 5, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7900551557540894})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6745628118515015})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6094419360160828})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6630674600601196})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6760692596435547})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6791372299194336})
store['active_learning_steps'][40]['training']['best_epoch']=3
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8902, 'crossentropy': 0.60047646484375}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 35435], ['ood', 59604], ['ood', 3811], ['ood', 58067], ['ood', 2154]], 'labels': [1, 1, 3, 5, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8209967613220215})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6813425421714783})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6620142459869385})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7303940057754517})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7213366031646729})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7321994304656982})
store['active_learning_steps'][41]['training']['best_epoch']=3
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8902, 'crossentropy': 0.613791357421875}
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 43042], ['ood', 49914], ['id', 14325], ['id', 43039], ['ood', 20606]], 'labels': [3, 7, 0, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.8659465312957764})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6034936308860779})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6791993975639343})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.686296284198761})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7815341949462891})
store['active_learning_steps'][42]['training']['best_epoch']=2
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.888, 'crossentropy': 0.60748828125}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 363], ['id', 3655], ['id', 13945], ['ood', 53862], ['id', 17616]], 'labels': [4, 3, 9, 8, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8406716585159302})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.691801905632019})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.719971776008606})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7679668664932251})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7908342480659485})
store['active_learning_steps'][43]['training']['best_epoch']=2
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8811, 'crossentropy': 0.618562548828125}
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 29832], ['ood', 39809], ['ood', 3917], ['ood', 44463], ['ood', 47235]], 'labels': [0, 4, 2, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8030531406402588})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7023596167564392})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6415329575538635})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6805018186569214})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7459956407546997})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7516573071479797})
store['active_learning_steps'][44]['training']['best_epoch']=3
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8838, 'crossentropy': 0.61792353515625}
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 22419], ['ood', 5087], ['ood', 35739], ['ood', 6676], ['id', 21992]], 'labels': [1, 1, 5, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8208036422729492})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6484124660491943})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6577181816101074})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7091711759567261})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7165138721466064})
store['active_learning_steps'][45]['training']['best_epoch']=2
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8859, 'crossentropy': 0.601501220703125}
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 6886], ['ood', 15176], ['ood', 24289], ['id', 20802], ['ood', 58301]], 'labels': [9, 9, 3, 1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9073524475097656})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7261326313018799})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6917917728424072})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.77305006980896})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7317522168159485})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7720741033554077})
store['active_learning_steps'][46]['training']['best_epoch']=3
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8893, 'crossentropy': 0.6391958984375}
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 35756], ['ood', 47164], ['ood', 1464], ['ood', 8957], ['id', 11035]], 'labels': [0, 9, 4, 5, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8906234502792358})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6588864326477051})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6745717525482178})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7469279766082764})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7250397801399231})
store['active_learning_steps'][47]['training']['best_epoch']=2
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8847, 'crossentropy': 0.593712744140625}
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 29291], ['ood', 17242], ['id', 36260], ['ood', 2898], ['ood', 403]], 'labels': [1, 6, 0, 4, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.926649808883667})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.641671895980835})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6420150399208069})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.700128436088562})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7177164554595947})
store['active_learning_steps'][48]['training']['best_epoch']=2
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8871, 'crossentropy': 0.620552001953125}
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 5468], ['ood', 58389], ['id', 19074], ['ood', 58792], ['id', 34099]], 'labels': [0, 6, 0, 9, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.828980028629303})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6086574792861938})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6217999458312988})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6711821556091309})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6667583584785461})
store['active_learning_steps'][49]['training']['best_epoch']=2
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8911, 'crossentropy': 0.58211201171875}
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 9684], ['id', 33883], ['ood', 4003], ['ood', 12892], ['ood', 52915]], 'labels': [0, 8, 3, 4, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8743181228637695})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6333942413330078})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5897513031959534})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7339636087417603})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8004834055900574})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7420325875282288})
store['active_learning_steps'][50]['training']['best_epoch']=3
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8937, 'crossentropy': 0.589984423828125}
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 59339], ['id', 12054], ['ood', 14203], ['id', 23945], ['id', 15532]], 'labels': [1, 8, 4, 9, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8586549758911133})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7277345657348633})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6973558664321899})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7561069130897522})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7109392881393433})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.791146993637085})
store['active_learning_steps'][51]['training']['best_epoch']=3
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8816, 'crossentropy': 0.673973095703125}
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 16670], ['ood', 44851], ['id', 22435], ['ood', 51557], ['ood', 37756]], 'labels': [1, 4, 6, 9, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7811303734779358})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6457629203796387})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6453742384910583})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6951826214790344})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8174716234207153})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.769658088684082})
store['active_learning_steps'][52]['training']['best_epoch']=3
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.8837, 'crossentropy': 0.639894189453125}
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 45072], ['ood', 6281], ['id', 5471], ['ood', 48992], ['ood', 37499]], 'labels': [0, 6, 3, 8, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8346854448318481})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6529042720794678})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6016272902488708})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6726200580596924})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6943491697311401})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6785615086555481})
store['active_learning_steps'][53]['training']['best_epoch']=3
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8943, 'crossentropy': 0.5777572265625}
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 23766], ['ood', 25045], ['id', 3804], ['id', 39401], ['ood', 43828]], 'labels': [4, 4, 7, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.890785276889801})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7174609899520874})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7326093912124634})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.731348991394043})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7790495157241821})
store['active_learning_steps'][54]['training']['best_epoch']=2
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8713, 'crossentropy': 0.67705419921875}
store['active_learning_steps'][54]['acquisition']={'indices': [['id', 55624], ['id', 46893], ['ood', 2999], ['id', 33332], ['ood', 35913]], 'labels': [0, 1, 5, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9546021819114685})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7323304414749146})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.737087070941925})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7530059814453125})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8619459867477417})
store['active_learning_steps'][55]['training']['best_epoch']=2
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.8597, 'crossentropy': 0.68692041015625}
store['active_learning_steps'][55]['acquisition']={'indices': [['id', 53269], ['ood', 22357], ['ood', 48500], ['ood', 18879], ['id', 27336]], 'labels': [2, 6, 0, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8577965497970581})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6293985843658447})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6477133631706238})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6864316463470459})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6446390151977539})
store['active_learning_steps'][56]['training']['best_epoch']=2
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8939, 'crossentropy': 0.589340234375}
store['active_learning_steps'][56]['acquisition']={'indices': [['ood', 159], ['ood', 30622], ['id', 51632], ['id', 10958], ['id', 22778]], 'labels': [2, 4, 9, 5, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8974249362945557})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6253336668014526})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.631606936454773})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6829969882965088})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6273260712623596})
store['active_learning_steps'][57]['training']['best_epoch']=2
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8829, 'crossentropy': 0.61541123046875}
store['active_learning_steps'][57]['acquisition']={'indices': [['ood', 5027], ['ood', 50441], ['ood', 7405], ['id', 1849], ['id', 31450]], 'labels': [2, 9, 4, 6, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.871727705001831})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6795833110809326})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6604194641113281})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7289013862609863})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6625897884368896})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6473042964935303})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7452222108840942})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6903273463249207})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7818604707717896})
store['active_learning_steps'][58]['training']['best_epoch']=6
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9038, 'crossentropy': 0.600862841796875}
store['active_learning_steps'][58]['acquisition']={'indices': [['id', 8075], ['ood', 56455], ['ood', 7361], ['ood', 46312], ['ood', 32131]], 'labels': [3, 4, 8, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8048431277275085})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6204923391342163})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.624791145324707})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7069000005722046})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6458153128623962})
store['active_learning_steps'][59]['training']['best_epoch']=2
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.8945, 'crossentropy': 0.566297021484375}
store['active_learning_steps'][59]['acquisition']={'indices': [['id', 4059], ['id', 41711], ['id', 30604], ['ood', 19196], ['ood', 3552]], 'labels': [6, 6, 7, 5, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9247126579284668})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6670828461647034})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6646641492843628})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6765347719192505})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6837023496627808})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6512960195541382})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6571205258369446})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.801416277885437})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7447737455368042})
store['active_learning_steps'][60]['training']['best_epoch']=6
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9064, 'crossentropy': 0.59273896484375}
store['active_learning_steps'][60]['acquisition']={'indices': [['id', 38391], ['ood', 52142], ['ood', 57771], ['ood', 38012], ['id', 9229]], 'labels': [8, 1, 8, 9, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.7888801097869873})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6584835648536682})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6621176600456238})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6447786092758179})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6646515130996704})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6453018188476562})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6638246774673462})
store['active_learning_steps'][61]['training']['best_epoch']=4
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9079, 'crossentropy': 0.5457140625}
store['active_learning_steps'][61]['acquisition']={'indices': [['id', 9148], ['ood', 11590], ['id', 18355], ['id', 56410], ['ood', 41307]], 'labels': [4, 4, 9, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.826530933380127})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5772744417190552})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5880105495452881})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6039725542068481})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6380881071090698})
store['active_learning_steps'][62]['training']['best_epoch']=2
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9004, 'crossentropy': 0.55132265625}
store['active_learning_steps'][62]['acquisition']={'indices': [['ood', 49198], ['id', 57595], ['id', 31037], ['ood', 54997], ['ood', 35469]], 'labels': [7, 0, 6, 9, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8313262462615967})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6444616317749023})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6601759791374207})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7542532682418823})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7236982583999634})
store['active_learning_steps'][63]['training']['best_epoch']=2
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.8839, 'crossentropy': 0.623608984375}
store['active_learning_steps'][63]['acquisition']={'indices': [['ood', 11281], ['id', 53566], ['id', 43678], ['id', 55229], ['ood', 16626]], 'labels': [9, 3, 6, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8981214165687561})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5910173058509827})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6024117469787598})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6099618673324585})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6896919012069702})
store['active_learning_steps'][64]['training']['best_epoch']=2
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9021, 'crossentropy': 0.535417578125}
store['active_learning_steps'][64]['acquisition']={'indices': [['id', 50609], ['ood', 36717], ['id', 49761], ['id', 522], ['id', 56847]], 'labels': [4, 4, 6, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8298034071922302})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5999623537063599})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5904514789581299})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6239290237426758})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6712785959243774})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7061470746994019})
store['active_learning_steps'][65]['training']['best_epoch']=3
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9054, 'crossentropy': 0.54028173828125}
store['active_learning_steps'][65]['acquisition']={'indices': [['id', 7419], ['ood', 59967], ['ood', 40074], ['id', 25297], ['ood', 8202]], 'labels': [5, 8, 0, 6, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.8445929288864136})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6024169325828552})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6121388077735901})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6494077444076538})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6742676496505737})
store['active_learning_steps'][66]['training']['best_epoch']=2
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.8965, 'crossentropy': 0.572972998046875}
store['active_learning_steps'][66]['acquisition']={'indices': [['ood', 12604], ['id', 24789], ['ood', 47253], ['id', 59761], ['ood', 37723]], 'labels': [4, 3, 3, 9, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8727959394454956})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6203387975692749})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6743873357772827})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7477743625640869})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7120325565338135})
store['active_learning_steps'][67]['training']['best_epoch']=2
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.8902, 'crossentropy': 0.5956658203125}
store['active_learning_steps'][67]['acquisition']={'indices': [['id', 16884], ['id', 792], ['id', 19951], ['ood', 35412], ['ood', 12009]], 'labels': [9, 8, 8, 5, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8169769048690796})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6098838448524475})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6038975715637207})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6394567489624023})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6175844669342041})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.642774760723114})
store['active_learning_steps'][68]['training']['best_epoch']=3
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9042, 'crossentropy': 0.54866630859375}
store['active_learning_steps'][68]['acquisition']={'indices': [['id', 19738], ['id', 30449], ['ood', 24160], ['id', 42931], ['id', 40869]], 'labels': [0, 7, 7, 3, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8261194229125977})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6072835922241211})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6314690709114075})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5881819128990173})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6107398867607117})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6365807056427002})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6031765937805176})
store['active_learning_steps'][69]['training']['best_epoch']=4
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9058, 'crossentropy': 0.5625357421875}
store['active_learning_steps'][69]['acquisition']={'indices': [['ood', 44279], ['ood', 47272], ['id', 55446], ['id', 16352], ['id', 38983]], 'labels': [3, 0, 7, 0, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8382570147514343})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5662485361099243})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5676107406616211})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6522905826568604})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5643137693405151})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5642020106315613})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6644400358200073})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6170591115951538})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6685481071472168})
store['active_learning_steps'][70]['training']['best_epoch']=6
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.911, 'crossentropy': 0.556876708984375}
store['active_learning_steps'][70]['acquisition']={'indices': [['id', 44715], ['ood', 9608], ['id', 15573], ['id', 21638], ['ood', 48385]], 'labels': [6, 6, 2, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8407257795333862})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.630547821521759})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5698445439338684})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5559475421905518})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5777379274368286})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.589613676071167})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6796315908432007})
store['active_learning_steps'][71]['training']['best_epoch']=4
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9123, 'crossentropy': 0.5222451171875}
store['active_learning_steps'][71]['acquisition']={'indices': [['id', 11218], ['id', 56455], ['ood', 50305], ['ood', 52993], ['id', 5086]], 'labels': [6, 6, 5, 8, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8616682291030884})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6158812046051025})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6399534940719604})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5848159193992615})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6407381892204285})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6043493747711182})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6332875490188599})
store['active_learning_steps'][72]['training']['best_epoch']=4
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.91, 'crossentropy': 0.524563330078125}
store['active_learning_steps'][72]['acquisition']={'indices': [['ood', 41621], ['ood', 1657], ['id', 28439], ['ood', 5944], ['ood', 59589]], 'labels': [3, 9, 1, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8524330854415894})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6081789135932922})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6154211759567261})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6157181262969971})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6513070464134216})
store['active_learning_steps'][73]['training']['best_epoch']=2
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.8951, 'crossentropy': 0.568201025390625}
store['active_learning_steps'][73]['acquisition']={'indices': [['id', 425], ['ood', 29521], ['id', 8392], ['ood', 17107], ['id', 8235]], 'labels': [3, 3, 5, 0, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7927870154380798})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6733462810516357})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5567317605018616})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5366184711456299})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5690889358520508})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5700686573982239})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5590223073959351})
store['active_learning_steps'][74]['training']['best_epoch']=4
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9134, 'crossentropy': 0.506594140625}
store['active_learning_steps'][74]['acquisition']={'indices': [['id', 50026], ['ood', 56562], ['id', 12096], ['ood', 41739], ['id', 43461]], 'labels': [0, 4, 9, 9, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9002628326416016})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6374782919883728})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6380399465560913})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5795194506645203})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6372700929641724})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6125872135162354})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6736277341842651})
store['active_learning_steps'][75]['training']['best_epoch']=4
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9062, 'crossentropy': 0.569633349609375}
store['active_learning_steps'][75]['acquisition']={'indices': [['ood', 22827], ['ood', 59562], ['ood', 44226], ['ood', 28615], ['ood', 54212]], 'labels': [3, 8, 1, 1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.782563328742981})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6200435161590576})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6023604869842529})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.592686653137207})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6095312833786011})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6703716516494751})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6126835346221924})
store['active_learning_steps'][76]['training']['best_epoch']=4
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9061, 'crossentropy': 0.55876181640625}
store['active_learning_steps'][76]['acquisition']={'indices': [['id', 47874], ['ood', 4045], ['ood', 40637], ['id', 21094], ['ood', 20504]], 'labels': [9, 8, 6, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.832554042339325})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5747857689857483})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5783467292785645})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6007951498031616})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6529332995414734})
store['active_learning_steps'][77]['training']['best_epoch']=2
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.8978, 'crossentropy': 0.5464748046875}
store['active_learning_steps'][77]['acquisition']={'indices': [['id', 57219], ['id', 36092], ['id', 24012], ['id', 55550], ['id', 50004]], 'labels': [9, 4, 2, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8546334505081177})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5853137969970703})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.646529495716095})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5642246007919312})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5934015512466431})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6877634525299072})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6920674443244934})
store['active_learning_steps'][78]['training']['best_epoch']=4
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9057, 'crossentropy': 0.556253271484375}
store['active_learning_steps'][78]['acquisition']={'indices': [['ood', 835], ['ood', 3504], ['id', 45046], ['ood', 51408], ['id', 38966]], 'labels': [3, 1, 3, 3, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8127869367599487})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5703725814819336})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5935877561569214})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5718910694122314})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5820334553718567})
store['active_learning_steps'][79]['training']['best_epoch']=2
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.8953, 'crossentropy': 0.56011552734375}
store['active_learning_steps'][79]['acquisition']={'indices': [['id', 55465], ['id', 53068], ['ood', 48034], ['id', 33568], ['ood', 32068]], 'labels': [9, 6, 7, 3, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8111433982849121})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5918771028518677})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5837448239326477})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6941637396812439})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5675475597381592})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5766891241073608})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6092634201049805})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5967386960983276})
store['active_learning_steps'][80]['training']['best_epoch']=5
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9189, 'crossentropy': 0.5405125}
store['active_learning_steps'][80]['acquisition']={'indices': [['ood', 28132], ['id', 567], ['ood', 27985], ['id', 27418], ['ood', 23269]], 'labels': [4, 7, 2, 8, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9176480770111084})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6457406878471375})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5720934271812439})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.607559084892273})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5914895534515381})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5816642045974731})
store['active_learning_steps'][81]['training']['best_epoch']=3
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9107, 'crossentropy': 0.500078564453125}
store['active_learning_steps'][81]['acquisition']={'indices': [['ood', 1733], ['ood', 9539], ['ood', 57130], ['ood', 28301], ['id', 22588]], 'labels': [5, 6, 9, 8, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8428479433059692})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6104292869567871})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.547433614730835})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5835867524147034})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5409736633300781})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6346390247344971})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6520047783851624})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6677002906799316})
store['active_learning_steps'][82]['training']['best_epoch']=5
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9162, 'crossentropy': 0.535553564453125}
store['active_learning_steps'][82]['acquisition']={'indices': [['id', 45152], ['ood', 34707], ['id', 31116], ['ood', 32707], ['id', 57158]], 'labels': [0, 5, 0, 7, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8491594791412354})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.609866738319397})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6192326545715332})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5631734132766724})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5628325939178467})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5409905910491943})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6026034951210022})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6328915357589722})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5439899563789368})
store['active_learning_steps'][83]['training']['best_epoch']=6
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.924, 'crossentropy': 0.494792041015625}
store['active_learning_steps'][83]['acquisition']={'indices': [['id', 30596], ['id', 54151], ['id', 26032], ['ood', 2914], ['id', 52893]], 'labels': [2, 5, 6, 3, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.816992998123169})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6156445741653442})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6032581329345703})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5805104970932007})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5431874990463257})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.570688009262085})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5294981002807617})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5331612825393677})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5851190686225891})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6259847283363342})
store['active_learning_steps'][84]['training']['best_epoch']=7
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9187, 'crossentropy': 0.51352158203125}
store['active_learning_steps'][84]['acquisition']={'indices': [['ood', 29411], ['id', 54212], ['id', 50639], ['ood', 8979], ['id', 31512]], 'labels': [6, 7, 8, 4, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.7868493795394897})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.579495906829834})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5520309209823608})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5345456600189209})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5821537971496582})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5349353551864624})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5398256778717041})
store['active_learning_steps'][85]['training']['best_epoch']=4
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9198, 'crossentropy': 0.465915576171875}
store['active_learning_steps'][85]['acquisition']={'indices': [['ood', 59215], ['id', 3899], ['ood', 37732], ['ood', 33647], ['ood', 57895]], 'labels': [1, 7, 1, 2, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8205225467681885})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5854418277740479})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6170027852058411})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6109131574630737})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6019880771636963})
store['active_learning_steps'][86]['training']['best_epoch']=2
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9056, 'crossentropy': 0.527404052734375}
