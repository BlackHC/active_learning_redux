store = {}
store['timestamp']=1620260126
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=27']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=27
store['worker_id']=27
store['num_workers']=40
store['config']={'seed': 34, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.2561469078063965})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.37519907951355})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.5818400382995605})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.778855800628662})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6971, 'crossentropy': 1.9335654296875}
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 14554], ['id', 22662], ['id', 41736], ['ood', 17098], ['id', 31066]], 'labels': [5, 7, 6, 9, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.7469313144683838})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.8082737922668457})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.1270973682403564})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.2070086002349854})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.709, 'crossentropy': 1.60566865234375}
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 20076], ['id', 38284], ['ood', 39207], ['ood', 38333], ['id', 31768]], 'labels': [0, 4, 6, 8, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.5246524810791016})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.9901537895202637})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.903144359588623})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.1674184799194336})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7001, 'crossentropy': 1.44537919921875}
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 43639], ['id', 45566], ['ood', 3356], ['ood', 36039], ['ood', 22409]], 'labels': [3, 6, 6, 4, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.6083441972732544})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.8500709533691406})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.8525772094726562})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.085172653198242})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6721, 'crossentropy': 1.44715390625}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 38010], ['id', 38057], ['id', 51467], ['id', 3416], ['id', 25454]], 'labels': [2, 0, 8, 5, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.612114429473877})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.9093683958053589})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.037553548812866})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.0551576614379883})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7074, 'crossentropy': 1.3592015625}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 53685], ['id', 30503], ['id', 44175], ['id', 50905], ['ood', 6507]], 'labels': [0, 2, 7, 7, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.4715397357940674})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.6710805892944336})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.8822481632232666})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.8522509336471558})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7139, 'crossentropy': 1.38394765625}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 6423], ['ood', 57907], ['id', 29570], ['ood', 46598], ['ood', 46553]], 'labels': [1, 8, 0, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.2974328994750977})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.5526087284088135})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.887699007987976})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.9580153226852417})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7346, 'crossentropy': 1.2332623046875}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 19425], ['id', 23502], ['ood', 56866], ['id', 26771], ['id', 8460]], 'labels': [3, 9, 7, 5, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.3013358116149902})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.5896244049072266})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.715637445449829})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.010345458984375})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7376, 'crossentropy': 1.23456005859375}
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 38689], ['ood', 25317], ['ood', 24497], ['ood', 36185], ['ood', 55553]], 'labels': [4, 5, 0, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.242821216583252})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.4239935874938965})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.5066205263137817})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.6305866241455078})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7464, 'crossentropy': 1.18292578125}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 13650], ['ood', 57495], ['ood', 2658], ['id', 47735], ['id', 29125]], 'labels': [4, 5, 6, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.3610410690307617})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.4768662452697754})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.8234703540802002})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.733407735824585})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7429, 'crossentropy': 1.2054638671875}
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 40112], ['ood', 24627], ['ood', 40046], ['id', 58896], ['id', 48249]], 'labels': [8, 0, 4, 2, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.1553658246994019})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.379507064819336})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.5333101749420166})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.7049726247787476})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7568, 'crossentropy': 1.13366787109375}
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 7664], ['ood', 9011], ['ood', 5180], ['id', 29737], ['ood', 48863]], 'labels': [4, 1, 5, 9, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.1950178146362305})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.3423799276351929})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.3802295923233032})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.4837749004364014})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7411, 'crossentropy': 1.12491337890625}
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 17943], ['id', 21751], ['ood', 18694], ['ood', 3279], ['ood', 40414]], 'labels': [9, 1, 4, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.207080364227295})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.3471202850341797})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.43295156955719})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.4556937217712402})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7336, 'crossentropy': 1.13591259765625}
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 27012], ['ood', 23308], ['id', 29673], ['id', 24556], ['id', 46436]], 'labels': [4, 0, 1, 9, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.2638511657714844})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.2314828634262085})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.5143764019012451})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.661332368850708})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.584199070930481})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.7612, 'crossentropy': 1.1955830078125}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 32373], ['id', 38434], ['ood', 12506], ['id', 54853], ['ood', 50429]], 'labels': [7, 8, 7, 0, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.226495385169983})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.3316706418991089})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.557829737663269})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.7462360858917236})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7404, 'crossentropy': 1.15652421875}
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 28165], ['id', 5333], ['id', 6216], ['id', 17511], ['id', 21901]], 'labels': [6, 8, 3, 4, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.0781911611557007})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.1416659355163574})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.314565658569336})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.4126675128936768})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.781, 'crossentropy': 1.039812890625}
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 52942], ['id', 45939], ['ood', 39952], ['ood', 38292], ['id', 46877]], 'labels': [1, 0, 5, 5, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.0991376638412476})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.0651609897613525})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.202331304550171})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.3738205432891846})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.3278965950012207})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.7818, 'crossentropy': 0.994535546875}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 22988], ['id', 33135], ['id', 29438], ['ood', 33545], ['id', 39433]], 'labels': [4, 6, 0, 6, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.090909481048584})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.0835987329483032})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.1401116847991943})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.1555547714233398})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.29450261592865})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8006, 'crossentropy': 0.99090888671875}
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 23370], ['id', 40204], ['ood', 2543], ['id', 18265], ['id', 11525]], 'labels': [3, 7, 3, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.1106741428375244})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.1013376712799072})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.1966941356658936})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.24430513381958})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.2599257230758667})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.7997, 'crossentropy': 0.99166494140625}
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 10895], ['ood', 26272], ['ood', 18683], ['ood', 41823], ['ood', 57026]], 'labels': [8, 8, 2, 6, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.0026326179504395})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.0976862907409668})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.1545133590698242})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.1256165504455566})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.7839, 'crossentropy': 0.9448412109375}
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 21048], ['id', 33303], ['ood', 31604], ['ood', 55033], ['ood', 1325]], 'labels': [5, 5, 7, 6, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.0019654035568237})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.0175458192825317})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.0362248420715332})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.241443395614624})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.789, 'crossentropy': 0.962981640625}
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 4375], ['id', 58248], ['ood', 7659], ['ood', 23048], ['ood', 8592]], 'labels': [2, 5, 4, 3, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 0.948226809501648})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9243899583816528})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.0413174629211426})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9852867126464844})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.1881287097930908})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8136, 'crossentropy': 0.89892158203125}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 37955], ['ood', 59548], ['id', 43766], ['id', 46687], ['id', 9723]], 'labels': [1, 5, 5, 2, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.0446608066558838})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.0619417428970337})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.100672721862793})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.2377430200576782})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.7753, 'crossentropy': 0.99384892578125}
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 10169], ['ood', 32005], ['ood', 48943], ['id', 4722], ['id', 33646]], 'labels': [8, 3, 0, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.0225979089736938})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.032799482345581})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.1436868906021118})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.2799831628799438})
store['active_learning_steps'][23]['training']['best_epoch']=1
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.7849, 'crossentropy': 0.97776728515625}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 13801], ['id', 4501], ['id', 33555], ['id', 44812], ['id', 18009]], 'labels': [9, 8, 5, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.0057554244995117})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9298731088638306})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.0231506824493408})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9621686935424805})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9956066608428955})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8202, 'crossentropy': 0.840492578125}
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 41573], ['ood', 59027], ['ood', 14627], ['id', 56751], ['ood', 749]], 'labels': [5, 9, 0, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 0.920035183429718})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.9091634154319763})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9862991571426392})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0313928127288818})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.0700116157531738})
store['active_learning_steps'][25]['training']['best_epoch']=2
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.82, 'crossentropy': 0.8334185546875}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 23197], ['ood', 17734], ['id', 9914], ['id', 20964], ['ood', 23220]], 'labels': [4, 2, 0, 9, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.8973729610443115})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.847956120967865})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8901259899139404})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9332234263420105})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9940696954727173})
store['active_learning_steps'][26]['training']['best_epoch']=2
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8298, 'crossentropy': 0.80302802734375}
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 2283], ['ood', 41331], ['id', 57330], ['id', 385], ['id', 44342]], 'labels': [7, 1, 5, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.0685205459594727})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.0716886520385742})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9587472677230835})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.071079969406128})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.1047348976135254})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.0676772594451904})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8289, 'crossentropy': 0.89366484375}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 42042], ['id', 53304], ['ood', 56596], ['ood', 30352], ['ood', 10539]], 'labels': [4, 1, 5, 4, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 0.9464683532714844})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.8695357441902161})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8971293568611145})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9635035991668701})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.906685471534729})
store['active_learning_steps'][28]['training']['best_epoch']=2
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8349, 'crossentropy': 0.763699609375}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 34429], ['id', 45083], ['ood', 42177], ['ood', 45763], ['ood', 55752]], 'labels': [4, 0, 8, 7, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 0.9630311727523804})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.8645509481430054})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9094324111938477})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.0102667808532715})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.00454843044281})
store['active_learning_steps'][29]['training']['best_epoch']=2
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8285, 'crossentropy': 0.800717529296875}
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 27126], ['ood', 53598], ['ood', 54091], ['id', 34821], ['ood', 57524]], 'labels': [4, 7, 9, 5, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.9231650233268738})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8498996496200562})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9097883701324463})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.017814040184021})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9816780090332031})
store['active_learning_steps'][30]['training']['best_epoch']=2
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8492, 'crossentropy': 0.74932666015625}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 55558], ['id', 3783], ['ood', 53341], ['id', 16874], ['ood', 37764]], 'labels': [6, 4, 2, 4, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 0.9862970113754272})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.850749135017395})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7804665565490723})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8831326365470886})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.887913703918457})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9092978835105896})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8656, 'crossentropy': 0.71367021484375}
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 47530], ['ood', 7828], ['id', 56550], ['ood', 51903], ['ood', 48752]], 'labels': [8, 7, 4, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.8874014616012573})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8436959981918335})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9166876077651978})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.880444347858429})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8963705897331238})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8376, 'crossentropy': 0.776196044921875}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 1586], ['id', 43521], ['ood', 5665], ['id', 41006], ['ood', 45967]], 'labels': [7, 9, 5, 4, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8836555480957031})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8545739650726318})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7751566171646118})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8824237585067749})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8676761388778687})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9290902614593506})
store['active_learning_steps'][33]['training']['best_epoch']=3
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8589, 'crossentropy': 0.75147109375}
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 13195], ['id', 32583], ['id', 2314], ['ood', 15296], ['ood', 21015]], 'labels': [4, 4, 2, 6, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.8722726106643677})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8067455887794495})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7344207167625427})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7601723670959473})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7597945928573608})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8972873687744141})
store['active_learning_steps'][34]['training']['best_epoch']=3
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8676, 'crossentropy': 0.66743369140625}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 30502], ['ood', 49300], ['id', 1373], ['id', 54715], ['ood', 2702]], 'labels': [7, 1, 4, 0, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 0.9429935812950134})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.8845257759094238})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8958426713943481})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8416457176208496})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8520588874816895})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9156203269958496})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9793933629989624})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8637, 'crossentropy': 0.8194154296875}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 34843], ['id', 53322], ['ood', 1657], ['ood', 17179], ['ood', 6789]], 'labels': [5, 2, 9, 4, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.9341545701026917})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9053314328193665})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.796777606010437})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8285794258117676})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8974006175994873})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.828639030456543})
store['active_learning_steps'][36]['training']['best_epoch']=3
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.857, 'crossentropy': 0.77269765625}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 49104], ['ood', 49057], ['id', 7643], ['ood', 35336], ['id', 24232]], 'labels': [6, 8, 7, 8, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.8880518078804016})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8255752325057983})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7411627769470215})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7846379280090332})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7762561440467834})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8002332448959351})
store['active_learning_steps'][37]['training']['best_epoch']=3
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8754, 'crossentropy': 0.6713658203125}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 2537], ['ood', 21622], ['id', 16745], ['ood', 13942], ['ood', 43013]], 'labels': [5, 4, 5, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.9096359610557556})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.7733228802680969})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7350977659225464})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7621924877166748})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7727248668670654})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8528201580047607})
store['active_learning_steps'][38]['training']['best_epoch']=3
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8781, 'crossentropy': 0.644652978515625}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 16989], ['id', 28285], ['id', 3350], ['ood', 20354], ['ood', 15339]], 'labels': [2, 2, 4, 9, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.9220176935195923})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.7491902709007263})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8082473278045654})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7593029737472534})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8394073843955994})
store['active_learning_steps'][39]['training']['best_epoch']=2
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8568, 'crossentropy': 0.697184326171875}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 26115], ['ood', 56043], ['id', 24458], ['ood', 4491], ['ood', 43678]], 'labels': [8, 5, 6, 2, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9086182117462158})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.7690455913543701})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8658092021942139})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7549423575401306})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7737388610839844})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7468554973602295})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8103015422821045})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7782562971115112})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.837550699710846})
store['active_learning_steps'][40]['training']['best_epoch']=6
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8905, 'crossentropy': 0.651528271484375}
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 10242], ['ood', 1822], ['ood', 29405], ['ood', 21544], ['id', 19551]], 'labels': [4, 1, 8, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 0.9413013458251953})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7006477117538452})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7521425485610962})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7573826313018799})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7742851376533508})
store['active_learning_steps'][41]['training']['best_epoch']=2
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8615, 'crossentropy': 0.66809619140625}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 32252], ['id', 13619], ['ood', 34747], ['ood', 16651], ['id', 18614]], 'labels': [7, 5, 1, 7, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.9023970365524292})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6476659774780273})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7216063141822815})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8497697114944458})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7392064332962036})
store['active_learning_steps'][42]['training']['best_epoch']=2
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.882, 'crossentropy': 0.631086572265625}
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 44582], ['id', 23137], ['id', 43375], ['id', 42552], ['ood', 15959]], 'labels': [0, 5, 4, 0, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 0.9144477844238281})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.7574737668037415})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6864404678344727})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6769461035728455})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8122835755348206})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8080416917800903})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8277332186698914})
store['active_learning_steps'][43]['training']['best_epoch']=4
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8846, 'crossentropy': 0.60666396484375}
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 43312], ['ood', 19224], ['id', 3196], ['ood', 42444], ['ood', 2112]], 'labels': [7, 1, 8, 5, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9096497297286987})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7675110697746277})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7158734798431396})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7534922957420349})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8099868297576904})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8553606271743774})
store['active_learning_steps'][44]['training']['best_epoch']=3
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8764, 'crossentropy': 0.672565234375}
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 13207], ['id', 55257], ['id', 32057], ['ood', 51184], ['id', 18897]], 'labels': [8, 3, 2, 8, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 0.9223620891571045})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.6952773332595825})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7399330139160156})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7683466672897339})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7424317598342896})
store['active_learning_steps'][45]['training']['best_epoch']=2
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8756, 'crossentropy': 0.6279525390625}
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 29491], ['id', 46184], ['ood', 49743], ['id', 26919], ['ood', 39567]], 'labels': [5, 3, 1, 8, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.8604792356491089})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7043584585189819})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.6869294047355652})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7584197521209717})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7350317239761353})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7298415899276733})
store['active_learning_steps'][46]['training']['best_epoch']=3
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8795, 'crossentropy': 0.6162642578125}
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 13774], ['id', 31671], ['ood', 7097], ['id', 4544], ['id', 32009]], 'labels': [2, 7, 6, 9, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8521215915679932})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7532507181167603})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7572702765464783})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7659478783607483})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7700774669647217})
store['active_learning_steps'][47]['training']['best_epoch']=2
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.875, 'crossentropy': 0.631627001953125}
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 27509], ['ood', 40829], ['ood', 6384], ['ood', 28047], ['id', 27982]], 'labels': [3, 3, 3, 2, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9060426950454712})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6771817803382874})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7165298461914062})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7428714036941528})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7762541770935059})
store['active_learning_steps'][48]['training']['best_epoch']=2
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8817, 'crossentropy': 0.623323681640625}
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 19180], ['ood', 14060], ['ood', 3712], ['ood', 993], ['id', 28222]], 'labels': [8, 2, 3, 4, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.8809523582458496})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7143392562866211})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7047393321990967})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7316784858703613})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7410569787025452})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7399972677230835})
store['active_learning_steps'][49]['training']['best_epoch']=3
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8861, 'crossentropy': 0.5946767578125}
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 31026], ['id', 57075], ['id', 3909], ['id', 4145], ['id', 21393]], 'labels': [8, 6, 7, 0, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 0.9595130681991577})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.7501040101051331})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6967264413833618})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7372593879699707})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7798748016357422})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.706210732460022})
store['active_learning_steps'][50]['training']['best_epoch']=3
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8832, 'crossentropy': 0.638569921875}
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 28705], ['id', 56442], ['ood', 51879], ['ood', 38389], ['ood', 28130]], 'labels': [4, 9, 8, 0, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9102773666381836})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7022756338119507})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6923649907112122})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.790905773639679})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8622366189956665})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7697381973266602})
store['active_learning_steps'][51]['training']['best_epoch']=3
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8914, 'crossentropy': 0.60291904296875}
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 36843], ['ood', 20497], ['ood', 13182], ['ood', 55520], ['id', 8363]], 'labels': [5, 0, 5, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.9173510074615479})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7655827403068542})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7749817371368408})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.750724196434021})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7651934623718262})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8529605865478516})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8720402121543884})
store['active_learning_steps'][52]['training']['best_epoch']=4
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.88, 'crossentropy': 0.663373828125}
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 8586], ['ood', 38695], ['id', 53955], ['id', 3784], ['id', 26964]], 'labels': [1, 1, 4, 9, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.9311447739601135})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7166602611541748})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6702052354812622})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7349430322647095})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7705689072608948})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6960642337799072})
store['active_learning_steps'][53]['training']['best_epoch']=3
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8935, 'crossentropy': 0.600520947265625}
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 23033], ['ood', 13033], ['ood', 11521], ['ood', 39561], ['id', 44656]], 'labels': [4, 1, 5, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.774248480796814})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6258713006973267})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7038341164588928})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6857309341430664})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7043799757957458})
store['active_learning_steps'][54]['training']['best_epoch']=2
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8932, 'crossentropy': 0.56290029296875}
store['active_learning_steps'][54]['acquisition']={'indices': [['ood', 6194], ['ood', 4098], ['id', 10757], ['ood', 21677], ['id', 7355]], 'labels': [2, 5, 3, 9, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9200936555862427})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6290175318717957})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.628919243812561})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6394587755203247})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6441758275032043})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6659374237060547})
store['active_learning_steps'][55]['training']['best_epoch']=3
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9029, 'crossentropy': 0.524234912109375}
store['active_learning_steps'][55]['acquisition']={'indices': [['ood', 10223], ['ood', 1787], ['ood', 57903], ['ood', 42834], ['id', 25930]], 'labels': [7, 3, 2, 1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.800868034362793})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.711321234703064})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6374833583831787})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.66143798828125})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6174050569534302})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8322921991348267})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7243573069572449})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6943830251693726})
store['active_learning_steps'][56]['training']['best_epoch']=5
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9066, 'crossentropy': 0.567656396484375}
store['active_learning_steps'][56]['acquisition']={'indices': [['ood', 10941], ['ood', 50457], ['id', 40358], ['ood', 18837], ['id', 35059]], 'labels': [8, 1, 7, 0, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8542677164077759})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6488729119300842})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6558364629745483})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6467057466506958})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7511398792266846})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6980284452438354})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.647738516330719})
store['active_learning_steps'][57]['training']['best_epoch']=4
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9043, 'crossentropy': 0.548709375}
store['active_learning_steps'][57]['acquisition']={'indices': [['ood', 9365], ['ood', 16716], ['ood', 7726], ['ood', 15058], ['id', 54232]], 'labels': [4, 3, 7, 9, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8242194056510925})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6429334282875061})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7462806105613708})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7434728145599365})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6987599730491638})
store['active_learning_steps'][58]['training']['best_epoch']=2
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.8911, 'crossentropy': 0.579153857421875}
store['active_learning_steps'][58]['acquisition']={'indices': [['ood', 28590], ['ood', 35412], ['id', 24357], ['ood', 35179], ['ood', 13266]], 'labels': [8, 5, 1, 3, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9276657104492188})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7406615018844604})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6931548118591309})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7385757565498352})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6393527388572693})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7859765291213989})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.685218334197998})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7771111726760864})
store['active_learning_steps'][59]['training']['best_epoch']=5
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.8971, 'crossentropy': 0.571610546875}
store['active_learning_steps'][59]['acquisition']={'indices': [['ood', 44201], ['id', 17439], ['ood', 23717], ['ood', 42596], ['ood', 19223]], 'labels': [9, 2, 1, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.891649603843689})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6317173838615417})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6488485336303711})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6651037335395813})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6983801126480103})
store['active_learning_steps'][60]['training']['best_epoch']=2
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8923, 'crossentropy': 0.58509619140625}
store['active_learning_steps'][60]['acquisition']={'indices': [['ood', 26628], ['id', 34502], ['ood', 10423], ['id', 30794], ['ood', 26746]], 'labels': [5, 0, 5, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.8561233878135681})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6615598201751709})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6066893339157104})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6826518774032593})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6431027054786682})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7174577116966248})
store['active_learning_steps'][61]['training']['best_epoch']=3
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9036, 'crossentropy': 0.51607021484375}
store['active_learning_steps'][61]['acquisition']={'indices': [['ood', 46284], ['ood', 22586], ['id', 31933], ['id', 4839], ['ood', 45719]], 'labels': [1, 6, 2, 4, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.855196475982666})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6740944385528564})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6021935939788818})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6196743845939636})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6574930548667908})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7438976764678955})
store['active_learning_steps'][62]['training']['best_epoch']=3
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9021, 'crossentropy': 0.54740986328125}
store['active_learning_steps'][62]['acquisition']={'indices': [['id', 4992], ['ood', 4144], ['id', 41321], ['ood', 45353], ['id', 10795]], 'labels': [8, 3, 5, 8, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.8958489298820496})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7180649638175964})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6602996587753296})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7559764385223389})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7731526494026184})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7281673550605774})
store['active_learning_steps'][63]['training']['best_epoch']=3
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.8903, 'crossentropy': 0.60562861328125}
store['active_learning_steps'][63]['acquisition']={'indices': [['ood', 2008], ['id', 50825], ['ood', 25388], ['id', 59077], ['ood', 18669]], 'labels': [2, 0, 9, 4, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8238017559051514})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6896315813064575})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6502454280853271})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6350153684616089})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7151493430137634})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7098731994628906})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6602634191513062})
store['active_learning_steps'][64]['training']['best_epoch']=4
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9052, 'crossentropy': 0.553556396484375}
store['active_learning_steps'][64]['acquisition']={'indices': [['id', 57661], ['id', 44476], ['ood', 56198], ['id', 59188], ['ood', 53225]], 'labels': [1, 5, 8, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9438554048538208})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6889514923095703})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6826468706130981})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7040035128593445})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6486390829086304})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7420477271080017})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7826114892959595})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.740792453289032})
store['active_learning_steps'][65]['training']['best_epoch']=5
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.8975, 'crossentropy': 0.59730712890625}
store['active_learning_steps'][65]['acquisition']={'indices': [['ood', 31393], ['id', 18134], ['ood', 35232], ['ood', 23301], ['id', 25705]], 'labels': [2, 6, 8, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 0.9504302144050598})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.6760709285736084})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7546908259391785})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6582381129264832})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7332782745361328})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7110463380813599})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7617400884628296})
store['active_learning_steps'][66]['training']['best_epoch']=4
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.898, 'crossentropy': 0.568893798828125}
store['active_learning_steps'][66]['acquisition']={'indices': [['id', 35639], ['id', 39294], ['ood', 44589], ['id', 51145], ['id', 57067]], 'labels': [0, 7, 9, 9, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.922313928604126})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.7897184491157532})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.706427812576294})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7245761156082153})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6948837637901306})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6976464986801147})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7504481077194214})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.714889645576477})
store['active_learning_steps'][67]['training']['best_epoch']=5
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9014, 'crossentropy': 0.573551611328125}
store['active_learning_steps'][67]['acquisition']={'indices': [['id', 9950], ['ood', 46402], ['id', 2545], ['id', 19335], ['ood', 57317]], 'labels': [9, 1, 6, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.9247254729270935})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.6846095323562622})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6701807975769043})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6837745904922485})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.704811692237854})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6793109178543091})
store['active_learning_steps'][68]['training']['best_epoch']=3
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.8917, 'crossentropy': 0.59973447265625}
store['active_learning_steps'][68]['acquisition']={'indices': [['id', 38132], ['id', 46260], ['ood', 38055], ['ood', 49665], ['id', 54849]], 'labels': [4, 7, 6, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.896634578704834})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7603656053543091})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.6998469829559326})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.753394603729248})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7949764132499695})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7333420515060425})
store['active_learning_steps'][69]['training']['best_epoch']=3
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.8909, 'crossentropy': 0.591089990234375}
store['active_learning_steps'][69]['acquisition']={'indices': [['ood', 2628], ['id', 34353], ['ood', 30221], ['ood', 48159], ['ood', 31622]], 'labels': [4, 7, 1, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.857770562171936})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6936596632003784})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6661077737808228})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6337459087371826})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6501791477203369})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6529090404510498})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7169443964958191})
store['active_learning_steps'][70]['training']['best_epoch']=4
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9051, 'crossentropy': 0.5599830078125}
store['active_learning_steps'][70]['acquisition']={'indices': [['ood', 13427], ['ood', 42271], ['id', 19167], ['id', 9918], ['id', 2332]], 'labels': [7, 2, 1, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.913163423538208})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.741563081741333})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6548478007316589})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6849173307418823})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7282000780105591})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6712665557861328})
store['active_learning_steps'][71]['training']['best_epoch']=3
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.897, 'crossentropy': 0.56211162109375}
store['active_learning_steps'][71]['acquisition']={'indices': [['id', 49143], ['ood', 28407], ['id', 7757], ['id', 21035], ['id', 20128]], 'labels': [9, 2, 9, 3, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8445142507553101})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6936410665512085})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6438506245613098})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6584557294845581})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6109689474105835})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.719902753829956})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6866568922996521})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6614083647727966})
store['active_learning_steps'][72]['training']['best_epoch']=5
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9114, 'crossentropy': 0.520569189453125}
store['active_learning_steps'][72]['acquisition']={'indices': [['ood', 33342], ['ood', 5254], ['id', 29308], ['id', 22989], ['id', 21423]], 'labels': [9, 0, 5, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9353950023651123})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6609161496162415})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6460304260253906})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6932796835899353})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6906219720840454})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6615540385246277})
store['active_learning_steps'][73]['training']['best_epoch']=3
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9038, 'crossentropy': 0.559997998046875}
store['active_learning_steps'][73]['acquisition']={'indices': [['id', 36510], ['ood', 29610], ['id', 39443], ['id', 22633], ['id', 42202]], 'labels': [9, 9, 4, 6, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8038771152496338})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6342904567718506})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6452035903930664})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6438848972320557})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6463495492935181})
store['active_learning_steps'][74]['training']['best_epoch']=2
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.8967, 'crossentropy': 0.543638720703125}
store['active_learning_steps'][74]['acquisition']={'indices': [['ood', 53109], ['ood', 22065], ['id', 58900], ['id', 26080], ['id', 37400]], 'labels': [3, 5, 6, 7, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8900285959243774})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.6619085073471069})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6147981882095337})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6732540130615234})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6340922117233276})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6839417219161987})
store['active_learning_steps'][75]['training']['best_epoch']=3
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.8977, 'crossentropy': 0.539469970703125}
store['active_learning_steps'][75]['acquisition']={'indices': [['id', 49386], ['ood', 45200], ['id', 48471], ['id', 35497], ['ood', 41505]], 'labels': [9, 6, 6, 6, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8817852139472961})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.584467351436615})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5917013883590698})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6166548728942871})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6848071813583374})
store['active_learning_steps'][76]['training']['best_epoch']=2
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.8957, 'crossentropy': 0.536289111328125}
store['active_learning_steps'][76]['acquisition']={'indices': [['id', 50065], ['id', 52497], ['id', 45756], ['ood', 3072], ['id', 47712]], 'labels': [2, 7, 9, 0, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8649223446846008})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6382300853729248})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6506209969520569})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6008131504058838})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.641171395778656})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6400084495544434})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5734642744064331})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6212799549102783})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6404716968536377})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6539139747619629})
store['active_learning_steps'][77]['training']['best_epoch']=7
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9155, 'crossentropy': 0.50158818359375}
store['active_learning_steps'][77]['acquisition']={'indices': [['ood', 27748], ['ood', 22240], ['ood', 35254], ['ood', 23616], ['id', 6781]], 'labels': [6, 6, 1, 7, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8537417054176331})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6482887268066406})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6165499687194824})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6149682402610779})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6551227569580078})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6824716925621033})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6486712098121643})
store['active_learning_steps'][78]['training']['best_epoch']=4
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9041, 'crossentropy': 0.535583203125}
store['active_learning_steps'][78]['acquisition']={'indices': [['ood', 40672], ['ood', 36837], ['ood', 11016], ['id', 18711], ['ood', 51925]], 'labels': [7, 5, 0, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8383579254150391})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6416900157928467})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5944453477859497})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6156290769577026})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.573983907699585})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6576226949691772})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6466495990753174})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.63954758644104})
store['active_learning_steps'][79]['training']['best_epoch']=5
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9149, 'crossentropy': 0.492541162109375}
store['active_learning_steps'][79]['acquisition']={'indices': [['ood', 4890], ['ood', 38307], ['ood', 51927], ['id', 996], ['id', 11873]], 'labels': [5, 3, 1, 6, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.8849697113037109})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6644362211227417})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6155539751052856})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6280079483985901})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6023347973823547})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6331992149353027})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7082216143608093})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6302008628845215})
store['active_learning_steps'][80]['training']['best_epoch']=5
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9158, 'crossentropy': 0.4849796875}
store['active_learning_steps'][80]['acquisition']={'indices': [['ood', 40071], ['ood', 43502], ['id', 55835], ['id', 44902], ['ood', 7709]], 'labels': [7, 4, 9, 2, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8775423765182495})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.644088625907898})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6456246376037598})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5769470930099487})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6386981010437012})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6231892704963684})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6515499949455261})
store['active_learning_steps'][81]['training']['best_epoch']=4
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9061, 'crossentropy': 0.517789794921875}
store['active_learning_steps'][81]['acquisition']={'indices': [['id', 41144], ['ood', 45580], ['id', 553], ['ood', 3103], ['id', 43079]], 'labels': [5, 1, 1, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8326252698898315})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6051955223083496})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.580470085144043})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5865401029586792})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5621752738952637})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6106325387954712})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6499384641647339})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6945383548736572})
store['active_learning_steps'][82]['training']['best_epoch']=5
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9103, 'crossentropy': 0.509898828125}
store['active_learning_steps'][82]['acquisition']={'indices': [['id', 41307], ['id', 25909], ['ood', 14101], ['ood', 54738], ['ood', 11584]], 'labels': [4, 9, 5, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8300304412841797})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6278136968612671})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5587723255157471})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5843592882156372})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5676413178443909})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6589822173118591})
store['active_learning_steps'][83]['training']['best_epoch']=3
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.899, 'crossentropy': 0.5243509765625}
store['active_learning_steps'][83]['acquisition']={'indices': [['id', 40787], ['ood', 16877], ['id', 39981], ['id', 18404], ['id', 48898]], 'labels': [8, 6, 3, 5, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7511083483695984})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5831731557846069})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5664857625961304})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.5956904292106628})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6429994106292725})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6171448230743408})
store['active_learning_steps'][84]['training']['best_epoch']=3
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9078, 'crossentropy': 0.48713779296875}
store['active_learning_steps'][84]['acquisition']={'indices': [['ood', 43187], ['ood', 30821], ['ood', 12599], ['id', 50151], ['ood', 44074]], 'labels': [4, 3, 8, 0, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8065056204795837})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.611751914024353})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.571696400642395})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5984479784965515})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6035411357879639})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6174790859222412})
store['active_learning_steps'][85]['training']['best_epoch']=3
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9067, 'crossentropy': 0.52159521484375}
store['active_learning_steps'][85]['acquisition']={'indices': [['id', 23823], ['ood', 55725], ['ood', 48610], ['ood', 38698], ['ood', 36235]], 'labels': [0, 4, 2, 4, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8539555668830872})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.675080418586731})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5864095091819763})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6307604312896729})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6705843210220337})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.641880452632904})
store['active_learning_steps'][86]['training']['best_epoch']=3
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9052, 'crossentropy': 0.53991455078125}
