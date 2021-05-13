store = {}
store['timestamp']=1620259916
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=22']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=22
store['worker_id']=22
store['num_workers']=40
store['config']={'seed': 24, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
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
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 55427], ['id', 40453], ['id', 3941], ['ood', 27940], ['ood', 12951]], 'labels': [0, 8, 3, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.0348570346832275})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.1879844665527344})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.328260898590088})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.2252278327941895})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6461, 'crossentropy': 1.68705625}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 34957], ['id', 40195], ['ood', 24421], ['ood', 14800], ['ood', 25085]], 'labels': [9, 8, 4, 6, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.5271202325820923})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.6855627298355103})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.81868577003479})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.9391968250274658})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6926, 'crossentropy': 1.37404365234375}
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 22436], ['id', 15949], ['ood', 23977], ['id', 183], ['id', 49018]], 'labels': [9, 5, 1, 9, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.435302734375})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.6007184982299805})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.7998974323272705})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.7509324550628662})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.706, 'crossentropy': 1.29594365234375}
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 58819], ['ood', 44622], ['ood', 10045], ['id', 48471], ['ood', 21645]], 'labels': [7, 9, 6, 6, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.3860207796096802})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.4244177341461182})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.6752711534500122})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.5553672313690186})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7096, 'crossentropy': 1.31588017578125}
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 6231], ['id', 8655], ['id', 47628], ['id', 26067], ['id', 5949]], 'labels': [2, 7, 3, 4, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.192507028579712})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.2978196144104004})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.3794900178909302})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.4721994400024414})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7389, 'crossentropy': 1.1823427734375}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 19212], ['id', 53699], ['ood', 16243], ['id', 24261], ['ood', 34594]], 'labels': [9, 7, 9, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.0342339277267456})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.1388579607009888})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.2468838691711426})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.3547422885894775})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7768, 'crossentropy': 1.001708984375}
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 38718], ['id', 20231], ['ood', 50043], ['id', 47570], ['ood', 28467]], 'labels': [6, 1, 4, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.0563969612121582})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.0385615825653076})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.2148040533065796})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.351995825767517})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.4333508014678955})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7862, 'crossentropy': 1.07165712890625}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 9588], ['ood', 7859], ['id', 30121], ['id', 51241], ['ood', 47592]], 'labels': [7, 8, 4, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9800381660461426})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.0731741189956665})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.0548710823059082})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.1199047565460205})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8096, 'crossentropy': 0.9749357421875}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 11828], ['ood', 48577], ['id', 11388], ['id', 33760], ['id', 23134]], 'labels': [6, 3, 9, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.1202843189239502})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.1626410484313965})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.2305731773376465})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.379063606262207})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7587, 'crossentropy': 1.137625390625}
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 42797], ['ood', 57742], ['ood', 54779], ['id', 2129], ['ood', 7772]], 'labels': [4, 9, 7, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.0723977088928223})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.0752363204956055})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.1042782068252563})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.2027792930603027})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7658, 'crossentropy': 1.09236416015625}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 39448], ['ood', 58906], ['ood', 36067], ['id', 24417], ['ood', 27963]], 'labels': [9, 8, 7, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9985085725784302})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9625807404518127})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.1340234279632568})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0260117053985596})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.1803631782531738})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8047, 'crossentropy': 1.00972314453125}
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 29179], ['ood', 33016], ['id', 48192], ['id', 45695], ['id', 12293]], 'labels': [3, 0, 8, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.0125441551208496})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.0473263263702393})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.114401936531067})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.145909070968628})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.793, 'crossentropy': 0.968973828125}
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 44293], ['ood', 3563], ['id', 16360], ['id', 6393], ['id', 41227]], 'labels': [2, 7, 9, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.0314428806304932})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.9625582098960876})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.0947057008743286})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.0804240703582764})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.171910047531128})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8101, 'crossentropy': 0.938204296875}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 32709], ['ood', 20951], ['id', 27297], ['id', 28785], ['ood', 27058]], 'labels': [3, 3, 1, 8, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.0390479564666748})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9403020143508911})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.1409327983856201})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.1096842288970947})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.1733934879302979})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.818, 'crossentropy': 0.9315091796875}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 32564], ['id', 43017], ['id', 26445], ['ood', 3479], ['id', 38293]], 'labels': [0, 1, 1, 7, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.9394841194152832})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9866853952407837})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0761425495147705})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.1320871114730835})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8058, 'crossentropy': 0.930319140625}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 799], ['id', 36123], ['ood', 1156], ['ood', 33320], ['id', 16539]], 'labels': [5, 2, 6, 5, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.036392092704773})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 0.9992280602455139})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9187540411949158})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0896053314208984})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.0849170684814453})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.1288368701934814})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8297, 'crossentropy': 0.913062109375}
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 19455], ['id', 2446], ['ood', 10274], ['id', 25030], ['ood', 33733]], 'labels': [7, 1, 6, 6, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.8754317760467529})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7968990802764893})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9823663234710693})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.993419349193573})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9362762570381165})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8434, 'crossentropy': 0.784195703125}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 44473], ['id', 9936], ['id', 14767], ['ood', 25406], ['ood', 51006]], 'labels': [1, 8, 1, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9981499910354614})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9703104496002197})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.0444189310073853})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.0320457220077515})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.030503511428833})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8191, 'crossentropy': 0.88978876953125}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 7173], ['ood', 52435], ['ood', 53484], ['id', 49234], ['ood', 56724]], 'labels': [7, 0, 8, 3, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.9619582891464233})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9362449645996094})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9899218082427979})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9875288009643555})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.1184083223342896})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8212, 'crossentropy': 0.8465826171875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 33613], ['ood', 1626], ['ood', 6026], ['id', 38519], ['ood', 38098]], 'labels': [1, 6, 5, 9, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8791890144348145})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8686180710792542})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9064750671386719})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9058660268783569})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9491342306137085})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8285, 'crossentropy': 0.82297919921875}
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 30828], ['ood', 15114], ['ood', 46298], ['id', 53858], ['ood', 51957]], 'labels': [1, 0, 0, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 0.9437066316604614})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8879868388175964})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8534319400787354})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.979870617389679})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.0471738576889038})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9918234944343567})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8341, 'crossentropy': 0.8547064453125}
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 24457], ['id', 19851], ['ood', 24781], ['id', 45658], ['ood', 48603]], 'labels': [6, 6, 8, 3, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 0.99720698595047})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9519102573394775})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9454846382141113})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9449247121810913})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.2454719543457031})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.086533546447754})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.158823847770691})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8255, 'crossentropy': 0.928372265625}
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 30488], ['ood', 27580], ['id', 49807], ['ood', 23828], ['ood', 6004]], 'labels': [2, 8, 1, 1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9268691539764404})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.896939754486084})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.0086090564727783})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9054232835769653})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9807630777359009})
store['active_learning_steps'][23]['training']['best_epoch']=2
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.831, 'crossentropy': 0.8251720703125}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 58798], ['ood', 49529], ['id', 20888], ['id', 23167], ['ood', 23148]], 'labels': [6, 2, 1, 1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.0227530002593994})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.0104670524597168})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9360034465789795})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9753158092498779})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.036379337310791})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.2164268493652344})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8304, 'crossentropy': 0.89704970703125}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 51208], ['id', 43698], ['id', 51437], ['id', 383], ['ood', 59686]], 'labels': [8, 8, 8, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9577513933181763})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8402489423751831})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9077461957931519})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8769274950027466})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.065746784210205})
store['active_learning_steps'][25]['training']['best_epoch']=2
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8303, 'crossentropy': 0.83320390625}
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 34698], ['ood', 24718], ['id', 23042], ['ood', 53719], ['id', 27083]], 'labels': [6, 9, 9, 6, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.0459930896759033})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9185640811920166})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.9478703737258911})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9551123380661011})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.0436232089996338})
store['active_learning_steps'][26]['training']['best_epoch']=2
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.815, 'crossentropy': 0.86432734375}
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 33945], ['ood', 59070], ['ood', 13357], ['ood', 5289], ['ood', 3863]], 'labels': [7, 6, 3, 4, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9612264037132263})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.9890382289886475})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9482588768005371})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9899905920028687})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.960626482963562})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.0144234895706177})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8195, 'crossentropy': 0.89976259765625}
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 11055], ['ood', 3634], ['id', 7707], ['ood', 53901], ['id', 40455]], 'labels': [2, 4, 0, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.0215394496917725})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8614839315414429})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9474432468414307})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9474447965621948})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.0088833570480347})
store['active_learning_steps'][28]['training']['best_epoch']=2
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8236, 'crossentropy': 0.83094287109375}
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 56168], ['ood', 4092], ['ood', 23532], ['ood', 30173], ['id', 54803]], 'labels': [6, 3, 5, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 0.9828438758850098})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8587465286254883})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.117959976196289})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0987015962600708})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.0958576202392578})
store['active_learning_steps'][29]['training']['best_epoch']=2
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8302, 'crossentropy': 0.816148095703125}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 58617], ['ood', 40756], ['ood', 30181], ['id', 45946], ['ood', 59351]], 'labels': [0, 4, 0, 3, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.033675193786621})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8173719644546509})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8773587346076965})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8694503307342529})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9567118883132935})
store['active_learning_steps'][30]['training']['best_epoch']=2
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8463, 'crossentropy': 0.760789697265625}
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 1426], ['ood', 28552], ['ood', 7807], ['id', 14636], ['id', 19547]], 'labels': [5, 8, 6, 3, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.0817651748657227})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.9306651949882507})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8386744260787964})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9759031534194946})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.0376896858215332})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.998725175857544})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8445, 'crossentropy': 0.766321484375}
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 54701], ['ood', 11785], ['ood', 9325], ['ood', 40618], ['id', 19501]], 'labels': [5, 8, 0, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.9451839327812195})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.8644148111343384})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.941225528717041})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.0538808107376099})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0183902978897095})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8415, 'crossentropy': 0.818151708984375}
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 34090], ['id', 42534], ['ood', 56155], ['id', 6296], ['id', 28492]], 'labels': [3, 3, 8, 0, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 0.9411734938621521})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8256739377975464})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9883891344070435})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.0791370868682861})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.0222944021224976})
store['active_learning_steps'][33]['training']['best_epoch']=2
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8484, 'crossentropy': 0.72004853515625}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 48994], ['id', 17155], ['id', 44278], ['id', 15934], ['id', 240]], 'labels': [6, 3, 0, 0, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.0668089389801025})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7392921447753906})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8407880663871765})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8722324371337891})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9329861402511597})
store['active_learning_steps'][34]['training']['best_epoch']=2
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8519, 'crossentropy': 0.75170341796875}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 5791], ['id', 27594], ['id', 23679], ['ood', 4089], ['ood', 22820]], 'labels': [8, 5, 0, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.0519975423812866})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8352844715118408})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8598853349685669})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8719481825828552})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8623520731925964})
store['active_learning_steps'][35]['training']['best_epoch']=2
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8225, 'crossentropy': 0.83521318359375}
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 16497], ['ood', 35123], ['ood', 41262], ['id', 24862], ['ood', 3896]], 'labels': [2, 9, 6, 2, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.054367184638977})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8139848709106445})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8162362575531006})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8708124160766602})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9108482599258423})
store['active_learning_steps'][36]['training']['best_epoch']=2
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8342, 'crossentropy': 0.805540625}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 55677], ['id', 32981], ['ood', 13348], ['ood', 29424], ['ood', 43630]], 'labels': [3, 2, 1, 1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.05422043800354})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8328088521957397})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7723183631896973})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8409807085990906})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8401724100112915})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.895599901676178})
store['active_learning_steps'][37]['training']['best_epoch']=3
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8658, 'crossentropy': 0.708207958984375}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 53206], ['ood', 13405], ['ood', 16093], ['id', 52665], ['ood', 2332]], 'labels': [1, 7, 5, 5, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 0.9397892355918884})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.8536557555198669})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8436266183853149})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8566412925720215})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9083215594291687})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0042052268981934})
store['active_learning_steps'][38]['training']['best_epoch']=3
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8417, 'crossentropy': 0.80450546875}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 31249], ['id', 2311], ['ood', 19617], ['id', 34416], ['ood', 58418]], 'labels': [3, 6, 3, 0, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9078819751739502})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8811701536178589})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.948412299156189})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8334730863571167})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.961410641670227})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8729778528213501})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9740011692047119})
store['active_learning_steps'][39]['training']['best_epoch']=4
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8717, 'crossentropy': 0.7175357421875}
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 16289], ['id', 51146], ['ood', 3701], ['id', 48266], ['ood', 23259]], 'labels': [9, 4, 1, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 0.8903169631958008})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7260849475860596})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7858245372772217})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8387355804443359})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.858007550239563})
store['active_learning_steps'][40]['training']['best_epoch']=2
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8632, 'crossentropy': 0.6831140625}
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 12010], ['id', 51064], ['ood', 5605], ['id', 23736], ['ood', 45989]], 'labels': [3, 2, 1, 5, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8732216358184814})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7886105179786682})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7891248464584351})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7800445556640625})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8098122477531433})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.809039294719696})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0111678838729858})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8735, 'crossentropy': 0.68474990234375}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 23250], ['ood', 48399], ['id', 22301], ['id', 47019], ['id', 15080]], 'labels': [0, 2, 7, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.8752858638763428})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7183558940887451})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7554057836532593})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7602159976959229})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7750338315963745})
store['active_learning_steps'][42]['training']['best_epoch']=2
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8665, 'crossentropy': 0.647650146484375}
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 8342], ['id', 39480], ['ood', 53412], ['ood', 47210], ['ood', 14253]], 'labels': [9, 9, 8, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.9030196666717529})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7657310366630554})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7621724605560303})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.709792971611023})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8051011562347412})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7423897981643677})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7910327911376953})
store['active_learning_steps'][43]['training']['best_epoch']=4
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8799, 'crossentropy': 0.628671484375}
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 43967], ['ood', 11346], ['id', 35628], ['ood', 48741], ['id', 2590]], 'labels': [1, 5, 5, 0, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 0.9299377202987671})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7016786336898804})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7175018787384033})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7910224199295044})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7689331769943237})
store['active_learning_steps'][44]['training']['best_epoch']=2
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8729, 'crossentropy': 0.633659521484375}
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 768], ['ood', 29750], ['ood', 20050], ['id', 5863], ['id', 56121]], 'labels': [5, 8, 7, 4, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9291520118713379})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7067686915397644})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7111032009124756})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7012405395507812})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.831382691860199})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.693488359451294})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8810439109802246})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8042022585868835})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8478862047195435})
store['active_learning_steps'][45]['training']['best_epoch']=6
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8907, 'crossentropy': 0.61851533203125}
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 48538], ['id', 36040], ['ood', 17437], ['id', 26776], ['ood', 3421]], 'labels': [6, 0, 8, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8693670034408569})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.6740838885307312})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.669183611869812})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6662454605102539})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6455338597297668})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8056514263153076})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6826261878013611})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7720786333084106})
store['active_learning_steps'][46]['training']['best_epoch']=5
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8887, 'crossentropy': 0.59221689453125}
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 55604], ['ood', 29905], ['id', 28146], ['id', 23112], ['id', 17297]], 'labels': [1, 9, 4, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8542566299438477})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6405742764472961})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6673843860626221})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7455211877822876})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7609345316886902})
store['active_learning_steps'][47]['training']['best_epoch']=2
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8804, 'crossentropy': 0.595851318359375}
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 40514], ['ood', 645], ['ood', 37103], ['ood', 23873], ['ood', 46347]], 'labels': [9, 0, 8, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9101659059524536})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7630752921104431})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6821485757827759})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7240581512451172})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7681255340576172})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7337621450424194})
store['active_learning_steps'][48]['training']['best_epoch']=3
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8816, 'crossentropy': 0.609331005859375}
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 35469], ['ood', 39647], ['ood', 25193], ['ood', 32398], ['ood', 36357]], 'labels': [9, 1, 8, 4, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.90993332862854})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7011972069740295})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7342837452888489})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6931161880493164})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8016666769981384})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7808812260627747})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7927671670913696})
store['active_learning_steps'][49]['training']['best_epoch']=4
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8893, 'crossentropy': 0.5830345703125}
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 7598], ['id', 27533], ['ood', 53265], ['ood', 38643], ['id', 29707]], 'labels': [6, 9, 6, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8895124197006226})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6743751764297485})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.735718846321106})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8276430368423462})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7590579390525818})
store['active_learning_steps'][50]['training']['best_epoch']=2
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8901, 'crossentropy': 0.603790087890625}
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 42051], ['id', 43562], ['ood', 48132], ['ood', 14471], ['id', 45689]], 'labels': [8, 3, 1, 1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.899077296257019})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.67103511095047})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6511446237564087})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7262512445449829})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7145408987998962})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7070715427398682})
store['active_learning_steps'][51]['training']['best_epoch']=3
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8853, 'crossentropy': 0.5614798828125}
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 23022], ['id', 6488], ['id', 7773], ['ood', 22019], ['ood', 30239]], 'labels': [3, 1, 9, 9, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9274164438247681})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6900734901428223})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6794383525848389})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7633128762245178})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7851698398590088})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8357130885124207})
store['active_learning_steps'][52]['training']['best_epoch']=3
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.896, 'crossentropy': 0.592551513671875}
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 32657], ['id', 16811], ['ood', 29703], ['id', 16854], ['ood', 8064]], 'labels': [9, 3, 3, 9, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8556135296821594})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6989407539367676})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6210842728614807})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6295793056488037})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7188129425048828})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6865408420562744})
store['active_learning_steps'][53]['training']['best_epoch']=3
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8901, 'crossentropy': 0.58840537109375}
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 27409], ['id', 5457], ['id', 45611], ['id', 23761], ['id', 59826]], 'labels': [1, 9, 4, 4, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.8397724032402039})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6564825773239136})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6441147327423096})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6261186599731445})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7074072360992432})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7692747116088867})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7280718088150024})
store['active_learning_steps'][54]['training']['best_epoch']=4
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.893, 'crossentropy': 0.6119142578125}
store['active_learning_steps'][54]['acquisition']={'indices': [['ood', 15016], ['id', 31749], ['ood', 41869], ['id', 35485], ['ood', 6975]], 'labels': [2, 8, 1, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8611420392990112})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7146462202072144})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6840768456459045})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6644602417945862})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7650811672210693})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7499635219573975})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7563900947570801})
store['active_learning_steps'][55]['training']['best_epoch']=4
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.8905, 'crossentropy': 0.618596875}
store['active_learning_steps'][55]['acquisition']={'indices': [['ood', 18887], ['ood', 26720], ['id', 56250], ['ood', 58596], ['id', 22869]], 'labels': [5, 2, 8, 8, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8427587151527405})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6127203106880188})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6409859657287598})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6690359115600586})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7286118865013123})
store['active_learning_steps'][56]['training']['best_epoch']=2
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.891, 'crossentropy': 0.559237060546875}
store['active_learning_steps'][56]['acquisition']={'indices': [['ood', 57304], ['id', 57315], ['ood', 39668], ['ood', 27849], ['id', 41697]], 'labels': [1, 8, 0, 3, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8139549493789673})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6163502931594849})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6904019117355347})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6475745439529419})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6465216875076294})
store['active_learning_steps'][57]['training']['best_epoch']=2
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8916, 'crossentropy': 0.59699873046875}
store['active_learning_steps'][57]['acquisition']={'indices': [['ood', 39906], ['ood', 44421], ['id', 14914], ['id', 24061], ['ood', 20354]], 'labels': [7, 2, 2, 9, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8639435768127441})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6678258776664734})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6591875553131104})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6207274198532104})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6812548041343689})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6546064019203186})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6636685132980347})
store['active_learning_steps'][58]['training']['best_epoch']=4
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.891, 'crossentropy': 0.570102587890625}
store['active_learning_steps'][58]['acquisition']={'indices': [['ood', 51564], ['id', 19550], ['id', 28129], ['id', 37925], ['ood', 58442]], 'labels': [4, 0, 9, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 0.9392168521881104})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7091245651245117})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6751428842544556})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6806968450546265})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7224293947219849})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7316839694976807})
store['active_learning_steps'][59]['training']['best_epoch']=3
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.8904, 'crossentropy': 0.586193212890625}
store['active_learning_steps'][59]['acquisition']={'indices': [['ood', 10766], ['id', 17376], ['id', 54573], ['id', 49144], ['ood', 33002]], 'labels': [2, 0, 2, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8285532593727112})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6743704080581665})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6447670459747314})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6630628108978271})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6903235912322998})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7127307057380676})
store['active_learning_steps'][60]['training']['best_epoch']=3
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8934, 'crossentropy': 0.576592529296875}
store['active_learning_steps'][60]['acquisition']={'indices': [['id', 12960], ['ood', 22345], ['id', 34393], ['id', 39968], ['id', 5367]], 'labels': [8, 8, 6, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8714970350265503})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5964672565460205})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6322831511497498})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6556315422058105})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.683444619178772})
store['active_learning_steps'][61]['training']['best_epoch']=2
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.8849, 'crossentropy': 0.58062890625}
store['active_learning_steps'][61]['acquisition']={'indices': [['id', 44820], ['ood', 8104], ['ood', 23710], ['id', 49485], ['id', 48713]], 'labels': [5, 0, 1, 7, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9220361709594727})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6954617500305176})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6686030030250549})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6952804327011108})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6985390186309814})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7060359716415405})
store['active_learning_steps'][62]['training']['best_epoch']=3
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.8803, 'crossentropy': 0.62012353515625}
store['active_learning_steps'][62]['acquisition']={'indices': [['ood', 33290], ['ood', 34953], ['id', 46659], ['id', 29582], ['ood', 59139]], 'labels': [0, 1, 9, 7, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8567568063735962})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7334741353988647})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6936230659484863})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6436330676078796})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7347552180290222})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.710320234298706})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7721854448318481})
store['active_learning_steps'][63]['training']['best_epoch']=4
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9008, 'crossentropy': 0.5834169921875}
store['active_learning_steps'][63]['acquisition']={'indices': [['id', 40415], ['ood', 44924], ['ood', 56821], ['id', 13484], ['id', 42638]], 'labels': [7, 4, 5, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8758223056793213})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6188294887542725})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5902736186981201})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6007318496704102})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6219650506973267})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.661596417427063})
store['active_learning_steps'][64]['training']['best_epoch']=3
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9072, 'crossentropy': 0.516043701171875}
store['active_learning_steps'][64]['acquisition']={'indices': [['ood', 17953], ['id', 24159], ['id', 21570], ['id', 42232], ['id', 19578]], 'labels': [6, 7, 3, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8573247194290161})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.645165205001831})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6472721099853516})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.639458954334259})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6294500827789307})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5767567157745361})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.659307599067688})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6120065450668335})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6935030817985535})
store['active_learning_steps'][65]['training']['best_epoch']=6
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9119, 'crossentropy': 0.523531689453125}
store['active_learning_steps'][65]['acquisition']={'indices': [['ood', 59049], ['ood', 28543], ['id', 49715], ['id', 40668], ['id', 40154]], 'labels': [8, 3, 8, 7, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8427252173423767})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6219503879547119})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6194415092468262})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6302529573440552})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6250355243682861})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.61799156665802})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6132915616035461})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6571622490882874})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6380892992019653})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6528906226158142})
store['active_learning_steps'][66]['training']['best_epoch']=7
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9123, 'crossentropy': 0.53722890625}
store['active_learning_steps'][66]['acquisition']={'indices': [['id', 30953], ['id', 50019], ['id', 10174], ['id', 15374], ['ood', 48360]], 'labels': [4, 5, 6, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8085592985153198})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5764347910881042})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5882598161697388})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6275874376296997})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6165093779563904})
store['active_learning_steps'][67]['training']['best_epoch']=2
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9027, 'crossentropy': 0.5408767578125}
store['active_learning_steps'][67]['acquisition']={'indices': [['ood', 59804], ['id', 50602], ['id', 44704], ['ood', 49917], ['id', 41542]], 'labels': [6, 5, 0, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.8533945679664612})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5892866849899292})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6204098463058472})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6747144460678101})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6945328712463379})
store['active_learning_steps'][68]['training']['best_epoch']=2
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.8989, 'crossentropy': 0.545972021484375}
store['active_learning_steps'][68]['acquisition']={'indices': [['id', 20057], ['ood', 34601], ['id', 39211], ['id', 31235], ['id', 41322]], 'labels': [6, 4, 5, 4, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8320448994636536})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5725104212760925})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5837653279304504})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5647493600845337})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5786854028701782})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6114214658737183})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6174482107162476})
store['active_learning_steps'][69]['training']['best_epoch']=4
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9151, 'crossentropy': 0.505193359375}
store['active_learning_steps'][69]['acquisition']={'indices': [['ood', 50110], ['ood', 31553], ['ood', 57893], ['id', 32362], ['ood', 43485]], 'labels': [7, 1, 7, 5, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.8705040216445923})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.64390629529953})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.626046895980835})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6413796544075012})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6978257894515991})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6802949905395508})
store['active_learning_steps'][70]['training']['best_epoch']=3
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9067, 'crossentropy': 0.523790625}
store['active_learning_steps'][70]['acquisition']={'indices': [['id', 28631], ['id', 13383], ['id', 58267], ['ood', 22117], ['ood', 48585]], 'labels': [2, 3, 2, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8639965057373047})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6186045408248901})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5892750024795532})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6002143621444702})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5701473951339722})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5854740142822266})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.671519935131073})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6274510622024536})
store['active_learning_steps'][71]['training']['best_epoch']=5
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9211, 'crossentropy': 0.47487978515625}
store['active_learning_steps'][71]['acquisition']={'indices': [['id', 21820], ['id', 36834], ['ood', 52129], ['id', 40661], ['ood', 5939]], 'labels': [5, 8, 0, 6, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8081574440002441})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5816669464111328})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6021851301193237})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5929872989654541})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6187946796417236})
store['active_learning_steps'][72]['training']['best_epoch']=2
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9105, 'crossentropy': 0.515689501953125}
store['active_learning_steps'][72]['acquisition']={'indices': [['ood', 45561], ['ood', 439], ['ood', 15132], ['id', 26430], ['id', 57796]], 'labels': [9, 3, 7, 9, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8964394927024841})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6943808794021606})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5934363603591919})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6634408831596375})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.627837061882019})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6594958901405334})
store['active_learning_steps'][73]['training']['best_epoch']=3
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9089, 'crossentropy': 0.53214755859375}
store['active_learning_steps'][73]['acquisition']={'indices': [['ood', 1712], ['id', 34770], ['id', 10991], ['id', 41316], ['id', 47114]], 'labels': [8, 8, 6, 6, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8290209770202637})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6046333312988281})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6445004940032959})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5980141162872314})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5984841585159302})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6186771392822266})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6410199403762817})
store['active_learning_steps'][74]['training']['best_epoch']=4
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9124, 'crossentropy': 0.51329453125}
store['active_learning_steps'][74]['acquisition']={'indices': [['id', 10415], ['id', 55407], ['id', 35801], ['id', 16382], ['ood', 43291]], 'labels': [3, 8, 3, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7884210348129272})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5508177280426025})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6161382794380188})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6078994274139404})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6137681007385254})
store['active_learning_steps'][75]['training']['best_epoch']=2
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9139, 'crossentropy': 0.511446435546875}
store['active_learning_steps'][75]['acquisition']={'indices': [['ood', 1013], ['ood', 4086], ['id', 28020], ['ood', 28035], ['ood', 35577]], 'labels': [0, 5, 4, 3, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7972496747970581})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5732120275497437})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5865442752838135})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5970766544342041})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6591885089874268})
store['active_learning_steps'][76]['training']['best_epoch']=2
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9018, 'crossentropy': 0.52700166015625}
store['active_learning_steps'][76]['acquisition']={'indices': [['ood', 22628], ['ood', 28610], ['ood', 30579], ['ood', 56712], ['ood', 11489]], 'labels': [3, 8, 4, 4, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7932173013687134})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5824154615402222})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5566552877426147})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.539606511592865})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5082868337631226})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5667606592178345})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6120607852935791})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5855756998062134})
store['active_learning_steps'][77]['training']['best_epoch']=5
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9209, 'crossentropy': 0.47444375}
store['active_learning_steps'][77]['acquisition']={'indices': [['ood', 28972], ['id', 56536], ['ood', 8235], ['ood', 11552], ['id', 51543]], 'labels': [5, 8, 2, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8027513027191162})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5740543603897095})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5432259440422058})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5375231504440308})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5478744506835938})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6255978941917419})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5423682928085327})
store['active_learning_steps'][78]['training']['best_epoch']=4
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9227, 'crossentropy': 0.456173193359375}
store['active_learning_steps'][78]['acquisition']={'indices': [['ood', 32002], ['ood', 46902], ['id', 53897], ['ood', 21202], ['id', 6058]], 'labels': [4, 6, 0, 9, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.819119930267334})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5816570520401001})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5553528070449829})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5495907664299011})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5050414800643921})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5342057943344116})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5912936329841614})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6117844581604004})
store['active_learning_steps'][79]['training']['best_epoch']=5
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9309, 'crossentropy': 0.425707470703125}
store['active_learning_steps'][79]['acquisition']={'indices': [['ood', 6512], ['ood', 48851], ['id', 22651], ['ood', 46371], ['ood', 31047]], 'labels': [8, 6, 7, 6, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7761536836624146})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5922046899795532})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.569490909576416})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5230922698974609})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5673810839653015})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5810343027114868})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5839897394180298})
store['active_learning_steps'][80]['training']['best_epoch']=4
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9263, 'crossentropy': 0.447016748046875}
store['active_learning_steps'][80]['acquisition']={'indices': [['ood', 5658], ['ood', 11281], ['id', 59138], ['id', 15537], ['ood', 24889]], 'labels': [3, 9, 7, 2, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8720062971115112})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6166620254516602})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5509361028671265})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5658929347991943})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6242411136627197})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5722193717956543})
store['active_learning_steps'][81]['training']['best_epoch']=3
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9127, 'crossentropy': 0.479676708984375}
store['active_learning_steps'][81]['acquisition']={'indices': [['ood', 53327], ['id', 24622], ['ood', 19403], ['ood', 25238], ['id', 16115]], 'labels': [7, 6, 0, 2, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9154938459396362})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6133686900138855})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5912718772888184})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5593868494033813})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6129670143127441})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6703307628631592})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6030443906784058})
store['active_learning_steps'][82]['training']['best_epoch']=4
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9182, 'crossentropy': 0.477846044921875}
store['active_learning_steps'][82]['acquisition']={'indices': [['ood', 14926], ['ood', 17658], ['id', 9013], ['id', 38622], ['ood', 26852]], 'labels': [8, 3, 1, 4, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8458970785140991})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5719252228736877})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5481210947036743})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5548953413963318})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5896371006965637})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5426395535469055})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5590205788612366})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6026490926742554})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5752588510513306})
store['active_learning_steps'][83]['training']['best_epoch']=6
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9235, 'crossentropy': 0.463194873046875}
store['active_learning_steps'][83]['acquisition']={'indices': [['ood', 29180], ['id', 37764], ['ood', 12372], ['ood', 8516], ['ood', 8245]], 'labels': [0, 9, 7, 9, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8038510084152222})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6097686886787415})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5245639681816101})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5813244581222534})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5838631391525269})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5682281255722046})
store['active_learning_steps'][84]['training']['best_epoch']=3
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9217, 'crossentropy': 0.476032861328125}
store['active_learning_steps'][84]['acquisition']={'indices': [['id', 36472], ['ood', 12885], ['ood', 10876], ['ood', 50147], ['ood', 59872]], 'labels': [7, 1, 2, 0, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8156067132949829})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6294826865196228})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5563057661056519})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5189251899719238})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4994382858276367})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5616788864135742})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5558850765228271})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5813478231430054})
store['active_learning_steps'][85]['training']['best_epoch']=5
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9237, 'crossentropy': 0.451142822265625}
store['active_learning_steps'][85]['acquisition']={'indices': [['ood', 2802], ['id', 45814], ['ood', 58446], ['id', 32596], ['ood', 47737]], 'labels': [4, 3, 5, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7951841354370117})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.579082727432251})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.49203282594680786})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.502884030342102})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5989020466804504})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5493848323822021})
store['active_learning_steps'][86]['training']['best_epoch']=3
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9204, 'crossentropy': 0.456785400390625}
