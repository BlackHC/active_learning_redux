store = {}
store['timestamp']=1620299926
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=39']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=39
store['worker_id']=39
store['num_workers']=40
store['config']={'seed': 58, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.872453212738037})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.3684964179992676})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.768110752105713})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.560546875, 'crossentropy': 4.009184837341309})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6362, 'crossentropy': 2.4240072265625}
store['active_learning_steps'][0]['acquisition']={'indices': [17282, 981, 31078, 6977, 19201], 'labels': [7, 7, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.2586822509765625})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.504800796508789})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.37974214553833})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.895857810974121})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6912, 'crossentropy': 2.1386044921875}
store['active_learning_steps'][1]['acquisition']={'indices': [55000, 34276, 51769, 14163, 39403], 'labels': [1, -1, 8, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.6426128149032593})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 2.0209851264953613})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.3965201377868652})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 2.1998486518859863})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7464, 'crossentropy': 1.70984453125}
store['active_learning_steps'][2]['acquisition']={'indices': [5571, 43582, 20452, 15009, 50336], 'labels': [-1, -1, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.6922051906585693})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.9798436164855957})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.2906832695007324})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 2.231429100036621})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7357, 'crossentropy': 1.673340234375}
store['active_learning_steps'][3]['acquisition']={'indices': [34139, 25287, 32952, 45484, 29187], 'labels': [5, 1, 0, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.5846658945083618})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.9323458671569824})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 2.155529022216797})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 2.330855369567871})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7631, 'crossentropy': 1.56482802734375}
store['active_learning_steps'][4]['acquisition']={'indices': [45436, 46467, 47493, 41724, 49544], 'labels': [-1, -1, 3, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.5763355493545532})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 2.0583486557006836})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 2.024425506591797})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 2.099562168121338})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7706, 'crossentropy': 1.4404189453125}
store['active_learning_steps'][5]['acquisition']={'indices': [4783, 24270, 49814, 5779, 47981], 'labels': [-1, -1, 3, 1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.4617793560028076})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.5875543355941772})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.8019534349441528})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 2.046630382537842})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7862, 'crossentropy': 1.32264501953125}
store['active_learning_steps'][6]['acquisition']={'indices': [39710, 43363, 15428, 54570, 12158], 'labels': [0, 8, 1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.4496734142303467})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.4674053192138672})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.6458866596221924})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.6972997188568115})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.784, 'crossentropy': 1.28496865234375}
store['active_learning_steps'][7]['acquisition']={'indices': [4562, 32423, 1231, 7310, 30047], 'labels': [5, 0, 7, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.3223674297332764})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.4768548011779785})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.675896406173706})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.819765329360962})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7985, 'crossentropy': 1.24774951171875}
store['active_learning_steps'][8]['acquisition']={'indices': [45310, 8534, 48045, 11897, 19730], 'labels': [-1, 4, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.4872069358825684})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.806266188621521})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.9144610166549683})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 2.0171406269073486})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7738, 'crossentropy': 1.4296685546875}
store['active_learning_steps'][9]['acquisition']={'indices': [1451, 1984, 36432, 49528, 39468], 'labels': [7, 9, 3, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.3655078411102295})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.4711835384368896})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.7126569747924805})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.7649645805358887})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7961, 'crossentropy': 1.2261400390625}
store['active_learning_steps'][10]['acquisition']={'indices': [27557, 33492, 27216, 44809, 16659], 'labels': [-1, 0, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.060043215751648})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.3890609741210938})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.549128532409668})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.6536537408828735})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8031, 'crossentropy': 1.0942171875}
store['active_learning_steps'][11]['acquisition']={'indices': [55088, 22519, 47915, 37031, 11918], 'labels': [-1, 7, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.3187572956085205})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.4391398429870605})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.6454960107803345})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.8310655355453491})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7991, 'crossentropy': 1.15886923828125}
store['active_learning_steps'][12]['acquisition']={'indices': [11553, 10467, 22786, 50244, 35203], 'labels': [7, -1, 4, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.2743144035339355})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.358424425125122})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.5252684354782104})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.4210463762283325})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8011, 'crossentropy': 1.136101953125}
store['active_learning_steps'][13]['acquisition']={'indices': [30989, 27138, 11244, 28009, 34867], 'labels': [6, -1, 3, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.3411650657653809})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.4544227123260498})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.8357123136520386})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.9297066926956177})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7895, 'crossentropy': 1.2656474609375}
store['active_learning_steps'][14]['acquisition']={'indices': [193, 16169, 2450, 46323, 17453], 'labels': [7, -1, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.1969900131225586})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.473869800567627})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.4651122093200684})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.519157886505127})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8042, 'crossentropy': 1.12267509765625}
store['active_learning_steps'][15]['acquisition']={'indices': [23675, 3083, 55974, 37530, 50087], 'labels': [-1, 9, 3, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.0415942668914795})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.2536108493804932})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.3016066551208496})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.3858940601348877})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8247, 'crossentropy': 0.99105244140625}
store['active_learning_steps'][16]['acquisition']={'indices': [26071, 23995, 54333, 22527, 27158], 'labels': [-1, 2, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.1785441637039185})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.1823792457580566})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.47885262966156})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.504811406135559})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.81, 'crossentropy': 1.10497041015625}
store['active_learning_steps'][17]['acquisition']={'indices': [10217, 30372, 12279, 4649, 5694], 'labels': [8, 1, 4, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9830225706100464})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.1971355676651})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.245943546295166})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.469854474067688})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8291, 'crossentropy': 1.0071244140625}
store['active_learning_steps'][18]['acquisition']={'indices': [32092, 4664, 47559, 31202, 47625], 'labels': [0, -1, 7, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.2323206663131714})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.243560791015625})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.3015074729919434})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.5926783084869385})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8114, 'crossentropy': 1.212679296875}
store['active_learning_steps'][19]['acquisition']={'indices': [59434, 4216, 2888, 20074, 4499], 'labels': [4, 0, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0690158605575562})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.2091279029846191})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.3895134925842285})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.5321838855743408})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8248, 'crossentropy': 1.0092994140625}
store['active_learning_steps'][20]['acquisition']={'indices': [2236, 20563, 36198, 55607, 44772], 'labels': [-1, -1, 0, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.178179383277893})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.378075122833252})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.3385844230651855})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.6407201290130615})
store['active_learning_steps'][21]['training']['best_epoch']=1
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8159, 'crossentropy': 1.11841357421875}
store['active_learning_steps'][21]['acquisition']={'indices': [52164, 3504, 38355, 4612, 47640], 'labels': [-1, -1, 0, 6, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.0280004739761353})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.1784696578979492})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.3704280853271484})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.4287352561950684})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8231, 'crossentropy': 0.988584375}
store['active_learning_steps'][22]['acquisition']={'indices': [58546, 49540, 15156, 8369, 18575], 'labels': [0, 7, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.1669793128967285})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.2443641424179077})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.3904650211334229})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.538571834564209})
store['active_learning_steps'][23]['training']['best_epoch']=1
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8181, 'crossentropy': 1.04695546875}
store['active_learning_steps'][23]['acquisition']={'indices': [54019, 48794, 47293, 43057, 46812], 'labels': [-1, -1, 4, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.0463180541992188})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.2126388549804688})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.528972864151001})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.5161513090133667})
store['active_learning_steps'][24]['training']['best_epoch']=1
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8315, 'crossentropy': 1.005713671875}
store['active_learning_steps'][24]['acquisition']={'indices': [30606, 39780, 17116, 8114, 32552], 'labels': [-1, 5, 3, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.1397879123687744})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.4308702945709229})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.5090261697769165})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.5399748086929321})
store['active_learning_steps'][25]['training']['best_epoch']=1
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8186, 'crossentropy': 1.076884765625}
store['active_learning_steps'][25]['acquisition']={'indices': [20472, 58732, 56570, 6260, 1472], 'labels': [8, 6, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0790386199951172})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.2988462448120117})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.3766968250274658})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.3674492835998535})
store['active_learning_steps'][26]['training']['best_epoch']=1
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8295, 'crossentropy': 0.98735986328125}
store['active_learning_steps'][26]['acquisition']={'indices': [19166, 1563, 40224, 7479, 3655], 'labels': [0, 2, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.0575456619262695})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.4639980792999268})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.2999610900878906})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.4794256687164307})
store['active_learning_steps'][27]['training']['best_epoch']=1
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8247, 'crossentropy': 1.02127890625}
store['active_learning_steps'][27]['acquisition']={'indices': [1981, 45028, 11279, 59467, 49415], 'labels': [3, 2, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.1158816814422607})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.1768732070922852})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1865246295928955})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.24001145362854})
store['active_learning_steps'][28]['training']['best_epoch']=1
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8305, 'crossentropy': 1.0161349609375}
store['active_learning_steps'][28]['acquisition']={'indices': [38431, 4329, 26335, 20928, 24274], 'labels': [-1, -1, 1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9332953691482544})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0695679187774658})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.1861469745635986})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.1793947219848633})
store['active_learning_steps'][29]['training']['best_epoch']=1
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.847, 'crossentropy': 0.90346796875}
store['active_learning_steps'][29]['acquisition']={'indices': [57872, 2367, 35359, 26013, 55560], 'labels': [-1, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9772999286651611})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0901720523834229})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.35127592086792})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.2400667667388916})
store['active_learning_steps'][30]['training']['best_epoch']=1
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.834, 'crossentropy': 0.9095900390625}
store['active_learning_steps'][30]['acquisition']={'indices': [30731, 19560, 50830, 17377, 35656], 'labels': [1, 9, 1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.0063542127609253})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.1858885288238525})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.2592447996139526})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.2632828950881958})
store['active_learning_steps'][31]['training']['best_epoch']=1
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8256, 'crossentropy': 0.96396787109375}
store['active_learning_steps'][31]['acquisition']={'indices': [26411, 35331, 58908, 31544, 11137], 'labels': [-1, -1, 5, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.960136353969574})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0238476991653442})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.2525255680084229})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.2380671501159668})
store['active_learning_steps'][32]['training']['best_epoch']=1
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8434, 'crossentropy': 0.905840234375}
store['active_learning_steps'][32]['acquisition']={'indices': [53301, 21002, 17301, 6570, 1552], 'labels': [-1, -1, 3, 1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.027267336845398})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9743120670318604})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.2001157999038696})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.1877689361572266})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.332193374633789})
store['active_learning_steps'][33]['training']['best_epoch']=2
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8583, 'crossentropy': 0.95003671875}
store['active_learning_steps'][33]['acquisition']={'indices': [25819, 19384, 40204, 6402, 7406], 'labels': [-1, -1, 7, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8384412527084351})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0251396894454956})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.1279644966125488})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.3127224445343018})
store['active_learning_steps'][34]['training']['best_epoch']=1
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.845, 'crossentropy': 0.8273720703125}
store['active_learning_steps'][34]['acquisition']={'indices': [43227, 36417, 40380, 7748, 24978], 'labels': [-1, 6, 1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8822188377380371})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.0130809545516968})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.1252148151397705})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.1181823015213013})
store['active_learning_steps'][35]['training']['best_epoch']=1
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8512, 'crossentropy': 0.844291015625}
store['active_learning_steps'][35]['acquisition']={'indices': [19637, 20196, 31008, 48491, 31142], 'labels': [-1, -1, -1, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.0817805528640747})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.1405673027038574})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.236513376235962})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.2973108291625977})
store['active_learning_steps'][36]['training']['best_epoch']=1
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.813, 'crossentropy': 0.947607421875}
store['active_learning_steps'][36]['acquisition']={'indices': [56866, 28331, 47001, 37979, 6730], 'labels': [8, -1, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.97010338306427})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0622203350067139})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0907396078109741})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.1997493505477905})
store['active_learning_steps'][37]['training']['best_epoch']=1
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8129, 'crossentropy': 0.9323087890625}
store['active_learning_steps'][37]['acquisition']={'indices': [51718, 11854, 35283, 52265, 15410], 'labels': [-1, -1, 9, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9276309609413147})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.0606865882873535})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.1306660175323486})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.2774810791015625})
store['active_learning_steps'][38]['training']['best_epoch']=1
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8369, 'crossentropy': 0.853669140625}
store['active_learning_steps'][38]['acquisition']={'indices': [13006, 41185, 38399, 32760, 40520], 'labels': [1, 5, 3, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8956699371337891})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0712060928344727})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.1522293090820312})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.2013444900512695})
store['active_learning_steps'][39]['training']['best_epoch']=1
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8397, 'crossentropy': 0.85534130859375}
store['active_learning_steps'][39]['acquisition']={'indices': [23383, 1155, 19081, 42800, 38003], 'labels': [8, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7999929189682007})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9869995713233948})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0218989849090576})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.0579581260681152})
store['active_learning_steps'][40]['training']['best_epoch']=1
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8601, 'crossentropy': 0.754793408203125}
store['active_learning_steps'][40]['acquisition']={'indices': [4870, 7078, 55699, 19040, 29519], 'labels': [0, -1, 7, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8311744928359985})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9703496694564819})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0909717082977295})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.1964619159698486})
store['active_learning_steps'][41]['training']['best_epoch']=1
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8516, 'crossentropy': 0.759894482421875}
store['active_learning_steps'][41]['acquisition']={'indices': [2058, 56270, 49853, 24519, 38819], 'labels': [0, -1, 0, 5, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9260309934616089})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.0193636417388916})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.0895042419433594})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.1567906141281128})
store['active_learning_steps'][42]['training']['best_epoch']=1
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8248, 'crossentropy': 0.86918427734375}
store['active_learning_steps'][42]['acquisition']={'indices': [45542, 25119, 41427, 48374, 6194], 'labels': [6, -1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.9282430410385132})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9442393779754639})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0668549537658691})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.0169832706451416})
store['active_learning_steps'][43]['training']['best_epoch']=1
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8202, 'crossentropy': 0.89450263671875}
store['active_learning_steps'][43]['acquisition']={'indices': [50987, 18934, 4249, 28983, 48835], 'labels': [-1, 5, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9193311929702759})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.896783173084259})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9481515884399414})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.134981393814087})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.086914300918579})
store['active_learning_steps'][44]['training']['best_epoch']=2
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8798, 'crossentropy': 0.748257861328125}
store['active_learning_steps'][44]['acquisition']={'indices': [21708, 6074, 22415, 31458, 13203], 'labels': [-1, 9, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9442752599716187})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.0612037181854248})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0955610275268555})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1038594245910645})
store['active_learning_steps'][45]['training']['best_epoch']=1
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.845, 'crossentropy': 0.847902734375}
store['active_learning_steps'][45]['acquisition']={'indices': [19951, 41574, 33729, 21366, 36794], 'labels': [8, 4, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7956161499023438})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.883219838142395})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.859300434589386})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9879938364028931})
store['active_learning_steps'][46]['training']['best_epoch']=1
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8558, 'crossentropy': 0.753675634765625}
store['active_learning_steps'][46]['acquisition']={'indices': [10152, 22619, 58446, 10546, 34271], 'labels': [1, 3, -1, 5, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9803301095962524})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9326649904251099})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0415804386138916})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.1073991060256958})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0809881687164307})
store['active_learning_steps'][47]['training']['best_epoch']=2
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8556, 'crossentropy': 0.9064275390625}
store['active_learning_steps'][47]['acquisition']={'indices': [3839, 4365, 41568, 21966, 53629], 'labels': [5, -1, 4, 3, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8372157216072083})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.922443151473999})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.920783281326294})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9715282917022705})
store['active_learning_steps'][48]['training']['best_epoch']=1
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8532, 'crossentropy': 0.774696337890625}
store['active_learning_steps'][48]['acquisition']={'indices': [41459, 55126, 44716, 43495, 53764], 'labels': [6, -1, -1, 2, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9080621004104614})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8377829790115356})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.979272723197937})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0466084480285645})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.118972897529602})
store['active_learning_steps'][49]['training']['best_epoch']=2
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8671, 'crossentropy': 0.8089828125}
store['active_learning_steps'][49]['acquisition']={'indices': [25002, 42138, 24752, 18695, 54113], 'labels': [-1, 2, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9058407545089722})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8940153121948242})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9286051988601685})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.064521074295044})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0908446311950684})
store['active_learning_steps'][50]['training']['best_epoch']=2
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8684, 'crossentropy': 0.83083037109375}
store['active_learning_steps'][50]['acquisition']={'indices': [42409, 31260, 919, 22981, 14835], 'labels': [-1, -1, 1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.8997156620025635})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9568473100662231})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.1020619869232178})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.14540433883667})
store['active_learning_steps'][51]['training']['best_epoch']=1
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8402, 'crossentropy': 0.84517646484375}
store['active_learning_steps'][51]['acquisition']={'indices': [33718, 10640, 37961, 50559, 17874], 'labels': [-1, 7, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.924299955368042})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9964971542358398})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9525351524353027})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.041117548942566})
store['active_learning_steps'][52]['training']['best_epoch']=1
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.8312, 'crossentropy': 0.8362751953125}
store['active_learning_steps'][52]['acquisition']={'indices': [31083, 24256, 2827, 7669, 56769], 'labels': [-1, -1, 4, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8980770111083984})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9759229421615601})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.1291520595550537})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8754900693893433})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.073941707611084})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.1088342666625977})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.0990900993347168})
store['active_learning_steps'][53]['training']['best_epoch']=4
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8858, 'crossentropy': 0.85587666015625}
store['active_learning_steps'][53]['acquisition']={'indices': [3051, 55746, 5141, 55461, 12028], 'labels': [-1, -1, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8463749885559082})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9115755558013916})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.0053004026412964})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.996673583984375})
store['active_learning_steps'][54]['training']['best_epoch']=1
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.844, 'crossentropy': 0.809703955078125}
store['active_learning_steps'][54]['acquisition']={'indices': [21565, 22628, 11601, 29028, 44142], 'labels': [6, 1, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 0.9360378980636597})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9755340814590454})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0373892784118652})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8840749263763428})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.164860486984253})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.050998330116272})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.0557494163513184})
store['active_learning_steps'][55]['training']['best_epoch']=4
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.886, 'crossentropy': 0.85229296875}
store['active_learning_steps'][55]['acquisition']={'indices': [31194, 26088, 8993, 2033, 50079], 'labels': [-1, 7, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8236392140388489})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.888299822807312})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0457745790481567})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9549937844276428})
store['active_learning_steps'][56]['training']['best_epoch']=1
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8496, 'crossentropy': 0.76657177734375}
store['active_learning_steps'][56]['acquisition']={'indices': [16178, 19780, 11719, 46352, 10750], 'labels': [0, -1, 3, 4, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8077746629714966})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8425161838531494})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.863782525062561})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9468179941177368})
store['active_learning_steps'][57]['training']['best_epoch']=1
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8656, 'crossentropy': 0.740154541015625}
store['active_learning_steps'][57]['acquisition']={'indices': [13297, 22420, 2907, 14346, 13100], 'labels': [-1, -1, 1, 1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.7963426113128662})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8626965284347534})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9670682549476624})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9941112995147705})
store['active_learning_steps'][58]['training']['best_epoch']=1
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.8644, 'crossentropy': 0.748797021484375}
store['active_learning_steps'][58]['acquisition']={'indices': [26039, 36358, 18928, 2843, 42951], 'labels': [6, -1, 9, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8907815217971802})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9054727554321289})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9130074977874756})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0421106815338135})
store['active_learning_steps'][59]['training']['best_epoch']=1
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.8386, 'crossentropy': 0.805114599609375}
store['active_learning_steps'][59]['acquisition']={'indices': [28493, 52294, 19549, 51886, 52600], 'labels': [4, 0, 3, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.8903471231460571})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8170864582061768})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9253913164138794})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9227153062820435})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 1.025285005569458})
store['active_learning_steps'][60]['training']['best_epoch']=2
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8753, 'crossentropy': 0.78542890625}
store['active_learning_steps'][60]['acquisition']={'indices': [21373, 13365, 50452, 18735, 31850], 'labels': [-1, -1, -1, 3, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8785185813903809})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8637458086013794})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.0162235498428345})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.0443215370178223})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 1.0221292972564697})
store['active_learning_steps'][61]['training']['best_epoch']=2
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.8683, 'crossentropy': 0.786204345703125}
store['active_learning_steps'][61]['acquisition']={'indices': [12901, 57449, 43623, 4822, 1534], 'labels': [-1, -1, 5, 4, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.852726936340332})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9561252593994141})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8957260251045227})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.144126534461975})
store['active_learning_steps'][62]['training']['best_epoch']=1
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.848, 'crossentropy': 0.784340380859375}
store['active_learning_steps'][62]['acquisition']={'indices': [27776, 2742, 59639, 40217, 44023], 'labels': [-1, 4, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.886600136756897})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9350822567939758})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0104329586029053})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9977467060089111})
store['active_learning_steps'][63]['training']['best_epoch']=1
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.8427, 'crossentropy': 0.7877921875}
store['active_learning_steps'][63]['acquisition']={'indices': [45061, 47612, 41116, 5135, 5799], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8801573514938354})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8069368600845337})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.965410590171814})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.1054472923278809})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.2230578660964966})
store['active_learning_steps'][64]['training']['best_epoch']=2
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.8778, 'crossentropy': 0.77004599609375}
store['active_learning_steps'][64]['acquisition']={'indices': [23885, 24753, 1902, 9932, 29], 'labels': [1, 6, -1, 3, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8011212348937988})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8565584421157837})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9873283505439758})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.104696273803711})
store['active_learning_steps'][65]['training']['best_epoch']=1
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.8415, 'crossentropy': 0.766272265625}
store['active_learning_steps'][65]['acquisition']={'indices': [54647, 29108, 50769, 47114, 37862], 'labels': [9, 9, 0, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8204587697982788})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8892726898193359})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9316534996032715})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9886052012443542})
store['active_learning_steps'][66]['training']['best_epoch']=1
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.8684, 'crossentropy': 0.71700029296875}
store['active_learning_steps'][66]['acquisition']={'indices': [5998, 29224, 7799, 54140, 49234], 'labels': [-1, -1, 8, 3, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8594272136688232})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9071158170700073})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9413425922393799})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 1.0021753311157227})
store['active_learning_steps'][67]['training']['best_epoch']=1
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.84, 'crossentropy': 0.816727099609375}
store['active_learning_steps'][67]['acquisition']={'indices': [42072, 56424, 4062, 35044, 7692], 'labels': [-1, 0, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8301914930343628})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9239369034767151})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9026364088058472})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.987412691116333})
store['active_learning_steps'][68]['training']['best_epoch']=1
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.8545, 'crossentropy': 0.749782958984375}
store['active_learning_steps'][68]['acquisition']={'indices': [10222, 15266, 55211, 4925, 51281], 'labels': [-1, 1, 8, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8792341947555542})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9499492049217224})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.952816903591156})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0605477094650269})
store['active_learning_steps'][69]['training']['best_epoch']=1
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.8478, 'crossentropy': 0.8625443359375}
store['active_learning_steps'][69]['acquisition']={'indices': [19794, 52710, 47507, 34221, 33772], 'labels': [4, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7867395877838135})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8443313837051392})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8008800745010376})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9293459057807922})
store['active_learning_steps'][70]['training']['best_epoch']=1
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.8562, 'crossentropy': 0.777159619140625}
store['active_learning_steps'][70]['acquisition']={'indices': [16250, 51305, 12662, 27105, 24148], 'labels': [-1, 1, 0, 8, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.882120668888092})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8227634429931641})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8871643543243408})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8985137939453125})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.9299266338348389})
store['active_learning_steps'][71]['training']['best_epoch']=2
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.881, 'crossentropy': 0.743374560546875}
store['active_learning_steps'][71]['acquisition']={'indices': [12532, 17824, 37065, 41124, 346], 'labels': [1, 9, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8372044563293457})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7221068143844604})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8093404769897461})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7775105834007263})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0051627159118652})
store['active_learning_steps'][72]['training']['best_epoch']=2
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.8845, 'crossentropy': 0.700158984375}
store['active_learning_steps'][72]['acquisition']={'indices': [54229, 36046, 5732, 51730, 43493], 'labels': [-1, 3, 1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8183358311653137})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8088661432266235})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8517404794692993})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9250640869140625})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.983811616897583})
store['active_learning_steps'][73]['training']['best_epoch']=2
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.8814, 'crossentropy': 0.765704296875}
store['active_learning_steps'][73]['acquisition']={'indices': [16361, 33154, 12379, 9278, 2202], 'labels': [-1, -1, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7959248423576355})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.851870596408844})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0040920972824097})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8705418109893799})
store['active_learning_steps'][74]['training']['best_epoch']=1
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.86, 'crossentropy': 0.761563671875}
store['active_learning_steps'][74]['acquisition']={'indices': [32437, 24483, 7419, 56557, 26022], 'labels': [-1, 1, -1, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7882858514785767})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7619170546531677})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8383359909057617})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9535747766494751})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8736363649368286})
store['active_learning_steps'][75]['training']['best_epoch']=2
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.8938, 'crossentropy': 0.6782623046875}
store['active_learning_steps'][75]['acquisition']={'indices': [2663, 7863, 30372, 7363, 27942], 'labels': [1, 4, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8027158379554749})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8646138906478882})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9427363872528076})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8383674621582031})
store['active_learning_steps'][76]['training']['best_epoch']=1
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.8526, 'crossentropy': 0.7583037109375}
store['active_learning_steps'][76]['acquisition']={'indices': [34547, 37572, 5820, 54656, 8752], 'labels': [-1, 3, 3, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8823244571685791})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8080881237983704})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8435423374176025})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8839622139930725})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9044152498245239})
store['active_learning_steps'][77]['training']['best_epoch']=2
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.8817, 'crossentropy': 0.732112451171875}
store['active_learning_steps'][77]['acquisition']={'indices': [14862, 11565, 22694, 19008, 12377], 'labels': [-1, 3, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8362758755683899})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6459312438964844})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7939486503601074})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8271360397338867})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9316356182098389})
store['active_learning_steps'][78]['training']['best_epoch']=2
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.8932, 'crossentropy': 0.667729931640625}
store['active_learning_steps'][78]['acquisition']={'indices': [50601, 16820, 17135, 3451, 24375], 'labels': [5, -1, 1, 6, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8208475112915039})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8210984468460083})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8330231308937073})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8587380647659302})
store['active_learning_steps'][79]['training']['best_epoch']=1
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.8606, 'crossentropy': 0.78395478515625}
store['active_learning_steps'][79]['acquisition']={'indices': [6924, 33470, 15134, 6801, 50323], 'labels': [8, -1, 6, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8476148247718811})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7652173638343811})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9839819073677063})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8456659317016602})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.885807991027832})
store['active_learning_steps'][80]['training']['best_epoch']=2
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.8804, 'crossentropy': 0.71497255859375}
store['active_learning_steps'][80]['acquisition']={'indices': [30298, 43704, 23087, 29107, 59437], 'labels': [-1, 1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7735506296157837})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8085222244262695})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.726737916469574})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.859599769115448})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8524203300476074})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8963920474052429})
store['active_learning_steps'][81]['training']['best_epoch']=3
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.8979, 'crossentropy': 0.69758818359375}
store['active_learning_steps'][81]['acquisition']={'indices': [31904, 22868, 18588, 11368, 50906], 'labels': [-1, -1, 3, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7722433805465698})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7784997820854187})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8329610824584961})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8436964154243469})
store['active_learning_steps'][82]['training']['best_epoch']=1
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.8594, 'crossentropy': 0.7646984375}
store['active_learning_steps'][82]['acquisition']={'indices': [15322, 58030, 20809, 21924, 16706], 'labels': [3, -1, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8079771995544434})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7641187906265259})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8412232995033264})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9410614371299744})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9082270264625549})
store['active_learning_steps'][83]['training']['best_epoch']=2
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.871, 'crossentropy': 0.715492236328125}
store['active_learning_steps'][83]['acquisition']={'indices': [14189, 44968, 25949, 2171, 59818], 'labels': [8, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8104491829872131})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.729474663734436})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8839069604873657})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7643476724624634})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.9364703893661499})
store['active_learning_steps'][84]['training']['best_epoch']=2
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.8892, 'crossentropy': 0.69650947265625}
store['active_learning_steps'][84]['acquisition']={'indices': [16786, 19816, 17942, 53611, 6254], 'labels': [-1, 1, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8160643577575684})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7451492547988892})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8858526945114136})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8517763614654541})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.9269287586212158})
store['active_learning_steps'][85]['training']['best_epoch']=2
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.8796, 'crossentropy': 0.736153955078125}
store['active_learning_steps'][85]['acquisition']={'indices': [3734, 23572, 4994, 54680, 38189], 'labels': [0, 3, 0, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8610371351242065})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8075395822525024})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8097752928733826})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9253738522529602})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.0480461120605469})
store['active_learning_steps'][86]['training']['best_epoch']=2
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.8819, 'crossentropy': 0.747436669921875}
store['active_learning_steps'][86]['acquisition']={'indices': [30255, 40434, 8709, 51040, 1399], 'labels': [-1, -1, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8743447661399841})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8294562697410583})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9419466257095337})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8391214609146118})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9172003269195557})
store['active_learning_steps'][87]['training']['best_epoch']=2
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.8694, 'crossentropy': 0.736811279296875}
store['active_learning_steps'][87]['acquisition']={'indices': [46090, 42239, 23458, 20522, 1843], 'labels': [0, 4, 8, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8726092576980591})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.693006157875061})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7431784868240356})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7732707858085632})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7966320514678955})
store['active_learning_steps'][88]['training']['best_epoch']=2
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.8938, 'crossentropy': 0.643218994140625}
store['active_learning_steps'][88]['acquisition']={'indices': [22080, 8901, 40296, 59472, 39595], 'labels': [9, -1, 8, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8232871294021606})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.745822548866272})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8594636917114258})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8301377296447754})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8592187166213989})
store['active_learning_steps'][89]['training']['best_epoch']=2
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.8921, 'crossentropy': 0.66867197265625}
store['active_learning_steps'][89]['acquisition']={'indices': [14420, 41012, 38754, 55111, 5817], 'labels': [3, 0, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8148688673973083})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.788490891456604})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8103286027908325})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8722066879272461})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.858089804649353})
store['active_learning_steps'][90]['training']['best_epoch']=2
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.8853, 'crossentropy': 0.696244140625}
store['active_learning_steps'][90]['acquisition']={'indices': [16229, 745, 59750, 28445, 36443], 'labels': [-1, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7864164710044861})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7068538665771484})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8930760622024536})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8971655368804932})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8402016758918762})
store['active_learning_steps'][91]['training']['best_epoch']=2
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.8905, 'crossentropy': 0.6610982421875}
store['active_learning_steps'][91]['acquisition']={'indices': [22856, 58219, 13232, 55853, 44055], 'labels': [-1, -1, 5, 8, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8807374238967896})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.780441403388977})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8429811000823975})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9159775972366333})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9480970501899719})
store['active_learning_steps'][92]['training']['best_epoch']=2
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.8891, 'crossentropy': 0.660312744140625}
store['active_learning_steps'][92]['acquisition']={'indices': [54801, 25956, 1191, 19196, 19454], 'labels': [-1, -1, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7410553693771362})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7004072666168213})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7854111790657043})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.894174337387085})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8225196599960327})
store['active_learning_steps'][93]['training']['best_epoch']=2
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.8895, 'crossentropy': 0.70909580078125}
store['active_learning_steps'][93]['acquisition']={'indices': [28101, 47582, 12911, 8304, 57062], 'labels': [0, -1, 2, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.7861429452896118})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7673140168190002})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8410443067550659})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8611520528793335})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8826844692230225})
store['active_learning_steps'][94]['training']['best_epoch']=2
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.8854, 'crossentropy': 0.70713759765625}
store['active_learning_steps'][94]['acquisition']={'indices': [48683, 13535, 45045, 46721, 31759], 'labels': [-1, 2, 7, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8212341070175171})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6987587213516235})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9020968675613403})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8823279142379761})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9781079292297363})
store['active_learning_steps'][95]['training']['best_epoch']=2
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.8965, 'crossentropy': 0.644035986328125}
store['active_learning_steps'][95]['acquisition']={'indices': [44285, 24032, 8830, 14130, 46981], 'labels': [-1, -1, -1, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8461748361587524})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.692348837852478})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7629334926605225})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8256475329399109})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8192428350448608})
store['active_learning_steps'][96]['training']['best_epoch']=2
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.8913, 'crossentropy': 0.632774951171875}
store['active_learning_steps'][96]['acquisition']={'indices': [34307, 7102, 52640, 3745, 34070], 'labels': [-1, -1, -1, 9, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.8529701232910156})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7465517520904541})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8786361217498779})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8249634504318237})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8855260014533997})
store['active_learning_steps'][97]['training']['best_epoch']=2
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.8889, 'crossentropy': 0.70748232421875}
store['active_learning_steps'][97]['acquisition']={'indices': [27129, 30882, 33257, 43155, 37446], 'labels': [4, -1, 0, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.854469895362854})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7220885753631592})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.834367036819458})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8130696415901184})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7961612939834595})
store['active_learning_steps'][98]['training']['best_epoch']=2
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.8917, 'crossentropy': 0.676174072265625}
store['active_learning_steps'][98]['acquisition']={'indices': [41509, 12960, 42063, 12207, 58906], 'labels': [-1, -1, 0, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.752490758895874})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8634325861930847})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9332984685897827})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9660677313804626})
store['active_learning_steps'][99]['training']['best_epoch']=1
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.859, 'crossentropy': 0.747568310546875}
store['active_learning_steps'][99]['acquisition']={'indices': [39500, 53250, 51229, 40587, 21602], 'labels': [-1, 9, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8441869616508484})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8482325077056885})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.881408154964447})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9119480848312378})
store['active_learning_steps'][100]['training']['best_epoch']=1
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.8589, 'crossentropy': 0.76581005859375}
store['active_learning_steps'][100]['acquisition']={'indices': [34747, 11162, 5047, 18517, 25456], 'labels': [2, -1, -1, 6, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][101]['training']={}
store['active_learning_steps'][101]['training']['epochs']=[]
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8246756792068481})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7695447206497192})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7929433584213257})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8898289203643799})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.920124888420105})
store['active_learning_steps'][101]['training']['best_epoch']=2
store['active_learning_steps'][101]['evaluation_metrics']={'accuracy': 0.8866, 'crossentropy': 0.70162119140625}
store['active_learning_steps'][101]['acquisition']={'indices': [26715, 12699, 35169, 47786, 13582], 'labels': [3, -1, -1, 0, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][102]['training']={}
store['active_learning_steps'][102]['training']['epochs']=[]
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8556442260742188})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8290354013442993})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8529432415962219})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8864968419075012})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.902182936668396})
store['active_learning_steps'][102]['training']['best_epoch']=2
store['active_learning_steps'][102]['evaluation_metrics']={'accuracy': 0.8796, 'crossentropy': 0.7807994140625}
store['active_learning_steps'][102]['acquisition']={'indices': [27270, 4791, 27144, 48101, 17356], 'labels': [-1, -1, 7, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][103]['training']={}
store['active_learning_steps'][103]['training']['epochs']=[]
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8226003646850586})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8379751443862915})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8026595115661621})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8081874847412109})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7583209872245789})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8796257376670837})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.9498786926269531})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.786200761795044})
store['active_learning_steps'][103]['training']['best_epoch']=5
store['active_learning_steps'][103]['evaluation_metrics']={'accuracy': 0.9042, 'crossentropy': 0.69157568359375}
store['active_learning_steps'][103]['acquisition']={'indices': [26248, 14113, 17122, 13217, 14711], 'labels': [8, -1, 0, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][104]['training']={}
store['active_learning_steps'][104]['training']['epochs']=[]
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8246976733207703})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.812021791934967})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8292791247367859})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.991075873374939})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9019432067871094})
store['active_learning_steps'][104]['training']['best_epoch']=2
store['active_learning_steps'][104]['evaluation_metrics']={'accuracy': 0.8805, 'crossentropy': 0.741493115234375}
store['active_learning_steps'][104]['acquisition']={'indices': [45721, 9200, 21785, 15707, 5637], 'labels': [0, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][105]['training']={}
store['active_learning_steps'][105]['training']['epochs']=[]
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8732044100761414})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7332767248153687})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6746424436569214})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.845666766166687})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7787044048309326})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8339207768440247})
store['active_learning_steps'][105]['training']['best_epoch']=3
store['active_learning_steps'][105]['evaluation_metrics']={'accuracy': 0.906, 'crossentropy': 0.6280171875}
store['active_learning_steps'][105]['acquisition']={'indices': [46843, 45703, 38122, 14295, 33782], 'labels': [-1, -1, 4, 2, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][106]['training']={}
store['active_learning_steps'][106]['training']['epochs']=[]
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7781422138214111})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7358295917510986})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8011285662651062})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8051446080207825})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8097777366638184})
store['active_learning_steps'][106]['training']['best_epoch']=2
store['active_learning_steps'][106]['evaluation_metrics']={'accuracy': 0.887, 'crossentropy': 0.667348388671875}
store['active_learning_steps'][106]['acquisition']={'indices': [16680, 42234, 25495, 27753, 54039], 'labels': [-1, -1, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][107]['training']={}
store['active_learning_steps'][107]['training']['epochs']=[]
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7947280406951904})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6995342969894409})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7636270523071289})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7401230335235596})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7890015244483948})
store['active_learning_steps'][107]['training']['best_epoch']=2
store['active_learning_steps'][107]['evaluation_metrics']={'accuracy': 0.8855, 'crossentropy': 0.675630078125}
store['active_learning_steps'][107]['acquisition']={'indices': [36621, 27041, 11782, 23588, 51110], 'labels': [0, 4, 5, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][108]['training']={}
store['active_learning_steps'][108]['training']['epochs']=[]
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7803912162780762})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7344462275505066})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7681391835212708})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7931532859802246})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8911058902740479})
store['active_learning_steps'][108]['training']['best_epoch']=2
store['active_learning_steps'][108]['evaluation_metrics']={'accuracy': 0.8892, 'crossentropy': 0.662576806640625}
store['active_learning_steps'][108]['acquisition']={'indices': [58756, 38034, 10164, 19654, 22575], 'labels': [-1, 7, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][109]['training']={}
store['active_learning_steps'][109]['training']['epochs']=[]
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7527637481689453})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7425419092178345})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7246649265289307})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8223232626914978})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8929873704910278})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.8647040724754333})
store['active_learning_steps'][109]['training']['best_epoch']=3
store['active_learning_steps'][109]['evaluation_metrics']={'accuracy': 0.9003, 'crossentropy': 0.65125478515625}
store['active_learning_steps'][109]['acquisition']={'indices': [20280, 31213, 15887, 39993, 36115], 'labels': [-1, 9, 2, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][110]['training']={}
store['active_learning_steps'][110]['training']['epochs']=[]
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8477419018745422})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7166951894760132})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7714381814002991})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7866668105125427})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7559921145439148})
store['active_learning_steps'][110]['training']['best_epoch']=2
store['active_learning_steps'][110]['evaluation_metrics']={'accuracy': 0.895, 'crossentropy': 0.664305615234375}
store['active_learning_steps'][110]['acquisition']={'indices': [43169, 15951, 20694, 38602, 3824], 'labels': [-1, -1, 7, 3, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][111]['training']={}
store['active_learning_steps'][111]['training']['epochs']=[]
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7129742503166199})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7264075875282288})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8188436031341553})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.755125105381012})
store['active_learning_steps'][111]['training']['best_epoch']=1
store['active_learning_steps'][111]['evaluation_metrics']={'accuracy': 0.8734, 'crossentropy': 0.693152392578125}
store['active_learning_steps'][111]['acquisition']={'indices': [22644, 52442, 35761, 52147, 43051], 'labels': [-1, 4, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][112]['training']={}
store['active_learning_steps'][112]['training']['epochs']=[]
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7775579690933228})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6827185153961182})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6789485216140747})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7572276592254639})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8066070675849915})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7895296216011047})
store['active_learning_steps'][112]['training']['best_epoch']=3
store['active_learning_steps'][112]['evaluation_metrics']={'accuracy': 0.9008, 'crossentropy': 0.616308447265625}
store['active_learning_steps'][112]['acquisition']={'indices': [51679, 12519, 5760, 40443, 17791], 'labels': [5, -1, 1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][113]['training']={}
store['active_learning_steps'][113]['training']['epochs']=[]
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.814232349395752})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7419725656509399})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7856122255325317})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7469689846038818})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8020589351654053})
store['active_learning_steps'][113]['training']['best_epoch']=2
store['active_learning_steps'][113]['evaluation_metrics']={'accuracy': 0.8898, 'crossentropy': 0.6442103515625}
store['active_learning_steps'][113]['acquisition']={'indices': [16934, 18230, 54984, 11674, 35678], 'labels': [-1, 2, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][114]['training']={}
store['active_learning_steps'][114]['training']['epochs']=[]
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8008114099502563})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7425645589828491})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8118829727172852})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7900846004486084})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8222233653068542})
store['active_learning_steps'][114]['training']['best_epoch']=2
store['active_learning_steps'][114]['evaluation_metrics']={'accuracy': 0.8932, 'crossentropy': 0.64838984375}
store['active_learning_steps'][114]['acquisition']={'indices': [24040, 25494, 27992, 27257, 59932], 'labels': [-1, 5, 6, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][115]['training']={}
store['active_learning_steps'][115]['training']['epochs']=[]
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7918596267700195})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7180054187774658})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7880139946937561})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.769597589969635})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8235350847244263})
store['active_learning_steps'][115]['training']['best_epoch']=2
store['active_learning_steps'][115]['evaluation_metrics']={'accuracy': 0.8951, 'crossentropy': 0.62549111328125}
store['active_learning_steps'][115]['acquisition']={'indices': [16538, 40928, 13277, 59533, 49218], 'labels': [-1, -1, -1, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][116]['training']={}
store['active_learning_steps'][116]['training']['epochs']=[]
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.829533576965332})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7580310106277466})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7736859321594238})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7433199882507324})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7941617965698242})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8767175674438477})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7528866529464722})
store['active_learning_steps'][116]['training']['best_epoch']=4
store['active_learning_steps'][116]['evaluation_metrics']={'accuracy': 0.9014, 'crossentropy': 0.700657373046875}
store['active_learning_steps'][116]['acquisition']={'indices': [43133, 32992, 16178, 47030, 9207], 'labels': [2, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][117]['training']={}
store['active_learning_steps'][117]['training']['epochs']=[]
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7785592675209045})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7143278121948242})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7389551401138306})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7075594663619995})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7581109404563904})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7958617806434631})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8683289289474487})
store['active_learning_steps'][117]['training']['best_epoch']=4
store['active_learning_steps'][117]['evaluation_metrics']={'accuracy': 0.9104, 'crossentropy': 0.65408369140625}
store['active_learning_steps'][117]['acquisition']={'indices': [15320, 7380, 24514, 328, 21856], 'labels': [-1, 7, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][118]['training']={}
store['active_learning_steps'][118]['training']['epochs']=[]
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8242228031158447})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6680008172988892})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6895012855529785})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7380671501159668})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8218047618865967})
store['active_learning_steps'][118]['training']['best_epoch']=2
store['active_learning_steps'][118]['evaluation_metrics']={'accuracy': 0.8948, 'crossentropy': 0.598162744140625}
store['active_learning_steps'][118]['acquisition']={'indices': [37246, 16063, 14507, 54325, 29045], 'labels': [-1, 5, 5, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][119]['training']={}
store['active_learning_steps'][119]['training']['epochs']=[]
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7131695747375488})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6997668743133545})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7739336490631104})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7087193727493286})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6583340167999268})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6643589735031128})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7881192564964294})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.8825581073760986})
store['active_learning_steps'][119]['training']['best_epoch']=5
store['active_learning_steps'][119]['evaluation_metrics']={'accuracy': 0.9157, 'crossentropy': 0.64637529296875}
store['active_learning_steps'][119]['acquisition']={'indices': [36078, 34936, 39913, 34685, 16200], 'labels': [-1, -1, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][120]['training']={}
store['active_learning_steps'][120]['training']['epochs']=[]
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.757980227470398})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6891394257545471})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.709384560585022})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7495055198669434})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7437328100204468})
store['active_learning_steps'][120]['training']['best_epoch']=2
store['active_learning_steps'][120]['evaluation_metrics']={'accuracy': 0.8891, 'crossentropy': 0.6403181640625}
store['active_learning_steps'][120]['acquisition']={'indices': [57964, 750, 29216, 1859, 54555], 'labels': [-1, 7, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][121]['training']={}
store['active_learning_steps'][121]['training']['epochs']=[]
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7309387922286987})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6610302329063416})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6424319744110107})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6546522378921509})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6910059452056885})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7464718222618103})
store['active_learning_steps'][121]['training']['best_epoch']=3
store['active_learning_steps'][121]['evaluation_metrics']={'accuracy': 0.9128, 'crossentropy': 0.5668005859375}
store['active_learning_steps'][121]['acquisition']={'indices': [11396, 29965, 24009, 144, 16398], 'labels': [-1, 8, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][122]['training']={}
store['active_learning_steps'][122]['training']['epochs']=[]
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7273489236831665})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7314941883087158})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7078083753585815})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7678513526916504})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.764743447303772})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.8465845584869385})
store['active_learning_steps'][122]['training']['best_epoch']=3
store['active_learning_steps'][122]['evaluation_metrics']={'accuracy': 0.8998, 'crossentropy': 0.63001005859375}
store['active_learning_steps'][122]['acquisition']={'indices': [38661, 26740, 17227, 52833, 49925], 'labels': [-1, -1, 3, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][123]['training']={}
store['active_learning_steps'][123]['training']['epochs']=[]
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7108003497123718})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6347862482070923})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7484655380249023})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7368876934051514})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7228482961654663})
store['active_learning_steps'][123]['training']['best_epoch']=2
store['active_learning_steps'][123]['evaluation_metrics']={'accuracy': 0.8975, 'crossentropy': 0.60242568359375}
store['active_learning_steps'][123]['acquisition']={'indices': [30832, 54294, 41924, 9979, 2452], 'labels': [2, -1, 9, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][124]['training']={}
store['active_learning_steps'][124]['training']['epochs']=[]
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.714841365814209})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6433964967727661})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6574245691299438})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.641889214515686})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6859329342842102})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7018190622329712})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7616455554962158})
store['active_learning_steps'][124]['training']['best_epoch']=4
store['active_learning_steps'][124]['evaluation_metrics']={'accuracy': 0.9153, 'crossentropy': 0.5812669921875}
store['active_learning_steps'][124]['acquisition']={'indices': [58171, 37953, 21269, 42412, 54257], 'labels': [1, 0, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][125]['training']={}
store['active_learning_steps'][125]['training']['epochs']=[]
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6994156241416931})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6659203767776489})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6014071106910706})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.68800950050354})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7559276819229126})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7166798114776611})
store['active_learning_steps'][125]['training']['best_epoch']=3
store['active_learning_steps'][125]['evaluation_metrics']={'accuracy': 0.9205, 'crossentropy': 0.50977060546875}
store['active_learning_steps'][125]['acquisition']={'indices': [16010, 32669, 35654, 13477, 9868], 'labels': [-1, -1, -1, 8, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][126]['training']={}
store['active_learning_steps'][126]['training']['epochs']=[]
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7700666189193726})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7038578391075134})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6342630982398987})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6816465854644775})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7519478797912598})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6785941123962402})
store['active_learning_steps'][126]['training']['best_epoch']=3
store['active_learning_steps'][126]['evaluation_metrics']={'accuracy': 0.9134, 'crossentropy': 0.562662744140625}
store['active_learning_steps'][126]['acquisition']={'indices': [34460, 9633, 42004, 53653, 12011], 'labels': [-1, -1, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][127]['training']={}
store['active_learning_steps'][127]['training']['epochs']=[]
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7793272733688354})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6259713172912598})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.689871609210968})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6255999207496643})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6502189040184021})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7688509225845337})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.7105603218078613})
store['active_learning_steps'][127]['training']['best_epoch']=4
store['active_learning_steps'][127]['evaluation_metrics']={'accuracy': 0.9146, 'crossentropy': 0.57060078125}
store['active_learning_steps'][127]['acquisition']={'indices': [13328, 51609, 24020, 2121, 29521], 'labels': [-1, 9, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][128]['training']={}
store['active_learning_steps'][128]['training']['epochs']=[]
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7810803055763245})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.586724042892456})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6011047959327698})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6435916423797607})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.700248122215271})
store['active_learning_steps'][128]['training']['best_epoch']=2
store['active_learning_steps'][128]['evaluation_metrics']={'accuracy': 0.8963, 'crossentropy': 0.55559423828125}
store['active_learning_steps'][128]['acquisition']={'indices': [9494, 8821, 153, 24831, 47424], 'labels': [-1, -1, 9, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][129]['training']={}
store['active_learning_steps'][129]['training']['epochs']=[]
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7262115478515625})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.623519778251648})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6909154057502747})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6921502351760864})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.68221515417099})
store['active_learning_steps'][129]['training']['best_epoch']=2
store['active_learning_steps'][129]['evaluation_metrics']={'accuracy': 0.908, 'crossentropy': 0.55586123046875}
store['active_learning_steps'][129]['acquisition']={'indices': [29864, 40811, 51335, 51492, 43504], 'labels': [4, 3, 7, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][130]['training']={}
store['active_learning_steps'][130]['training']['epochs']=[]
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6818593144416809})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6052402257919312})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6340482234954834})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6259483098983765})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6476471424102783})
store['active_learning_steps'][130]['training']['best_epoch']=2
store['active_learning_steps'][130]['evaluation_metrics']={'accuracy': 0.9044, 'crossentropy': 0.53695537109375}
store['active_learning_steps'][130]['acquisition']={'indices': [40850, 36445, 55800, 5636, 46409], 'labels': [0, 8, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][131]['training']={}
store['active_learning_steps'][131]['training']['epochs']=[]
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7281093597412109})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5895357131958008})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6240315437316895})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6688600182533264})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7063038945198059})
store['active_learning_steps'][131]['training']['best_epoch']=2
store['active_learning_steps'][131]['evaluation_metrics']={'accuracy': 0.9083, 'crossentropy': 0.528881787109375}
store['active_learning_steps'][131]['acquisition']={'indices': [10974, 27121, 26850, 54942, 8561], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][132]['training']={}
store['active_learning_steps'][132]['training']['epochs']=[]
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7204828262329102})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6030052900314331})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5707517862319946})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6458090543746948})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6674848794937134})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6455726027488708})
store['active_learning_steps'][132]['training']['best_epoch']=3
store['active_learning_steps'][132]['evaluation_metrics']={'accuracy': 0.9168, 'crossentropy': 0.525855126953125}
store['active_learning_steps'][132]['acquisition']={'indices': [54790, 18406, 49167, 11558, 6992], 'labels': [2, 8, 1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][133]['training']={}
store['active_learning_steps'][133]['training']['epochs']=[]
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6881210803985596})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5859509706497192})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6288275718688965})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6310777068138123})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.65610671043396})
store['active_learning_steps'][133]['training']['best_epoch']=2
store['active_learning_steps'][133]['evaluation_metrics']={'accuracy': 0.9017, 'crossentropy': 0.561599169921875}
store['active_learning_steps'][133]['acquisition']={'indices': [49968, 33091, 57095, 1388, 50060], 'labels': [-1, 1, 1, 8, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][134]['training']={}
store['active_learning_steps'][134]['training']['epochs']=[]
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.714751124382019})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5893357992172241})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5860200524330139})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6412692070007324})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6534111499786377})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6726111173629761})
store['active_learning_steps'][134]['training']['best_epoch']=3
store['active_learning_steps'][134]['evaluation_metrics']={'accuracy': 0.9066, 'crossentropy': 0.56041484375}
store['active_learning_steps'][134]['acquisition']={'indices': [54865, 36193, 5946, 34977, 25153], 'labels': [0, 5, 7, 0, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][135]['training']={}
store['active_learning_steps'][135]['training']['epochs']=[]
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7232239246368408})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6635655760765076})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.608605146408081})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7200173139572144})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7136316895484924})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7321768999099731})
store['active_learning_steps'][135]['training']['best_epoch']=3
store['active_learning_steps'][135]['evaluation_metrics']={'accuracy': 0.9082, 'crossentropy': 0.56041552734375}
store['active_learning_steps'][135]['acquisition']={'indices': [6662, 14620, 36105, 47746, 44528], 'labels': [3, 4, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][136]['training']={}
store['active_learning_steps'][136]['training']['epochs']=[]
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6399860978126526})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5802483558654785})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5603266954421997})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5905839204788208})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6270182132720947})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6473942995071411})
store['active_learning_steps'][136]['training']['best_epoch']=3
store['active_learning_steps'][136]['evaluation_metrics']={'accuracy': 0.916, 'crossentropy': 0.508915087890625}
store['active_learning_steps'][136]['acquisition']={'indices': [47333, 1934, 41986, 33173, 15005], 'labels': [1, 4, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][137]['training']={}
store['active_learning_steps'][137]['training']['epochs']=[]
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6182064414024353})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5863484144210815})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.631036102771759})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5855585336685181})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5899115800857544})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6482570171356201})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6764076352119446})
store['active_learning_steps'][137]['training']['best_epoch']=4
store['active_learning_steps'][137]['evaluation_metrics']={'accuracy': 0.9171, 'crossentropy': 0.529310546875}
store['active_learning_steps'][137]['acquisition']={'indices': [29798, 51324, 32432, 16207, 45679], 'labels': [8, 8, 7, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][138]['training']={}
store['active_learning_steps'][138]['training']['epochs']=[]
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.7395353317260742})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5872921943664551})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6515965461730957})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6272870898246765})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6864484548568726})
store['active_learning_steps'][138]['training']['best_epoch']=2
store['active_learning_steps'][138]['evaluation_metrics']={'accuracy': 0.8985, 'crossentropy': 0.569510595703125}
store['active_learning_steps'][138]['acquisition']={'indices': [32474, 38803, 35777, 8787, 40194], 'labels': [1, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][139]['training']={}
store['active_learning_steps'][139]['training']['epochs']=[]
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6893091201782227})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5914772748947144})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.623842716217041})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6637825965881348})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6449559926986694})
store['active_learning_steps'][139]['training']['best_epoch']=2
store['active_learning_steps'][139]['evaluation_metrics']={'accuracy': 0.9047, 'crossentropy': 0.534075146484375}
store['active_learning_steps'][139]['acquisition']={'indices': [39437, 1014, 23487, 18839, 58760], 'labels': [1, 7, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][140]['training']={}
store['active_learning_steps'][140]['training']['epochs']=[]
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6960006356239319})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5671977996826172})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6009886860847473})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6480695009231567})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5778079032897949})
store['active_learning_steps'][140]['training']['best_epoch']=2
store['active_learning_steps'][140]['evaluation_metrics']={'accuracy': 0.9031, 'crossentropy': 0.549546240234375}
store['active_learning_steps'][140]['acquisition']={'indices': [47593, 44778, 42547, 16594, 33871], 'labels': [6, 9, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][141]['training']={}
store['active_learning_steps'][141]['training']['epochs']=[]
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7322182059288025})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5823650360107422})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6748265624046326})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7158721089363098})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7558166980743408})
store['active_learning_steps'][141]['training']['best_epoch']=2
store['active_learning_steps'][141]['evaluation_metrics']={'accuracy': 0.9059, 'crossentropy': 0.55334091796875}
store['active_learning_steps'][141]['acquisition']={'indices': [31528, 33450, 58820, 54845, 50741], 'labels': [8, -1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][142]['training']={}
store['active_learning_steps'][142]['training']['epochs']=[]
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7468151450157166})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5864840745925903})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6152197122573853})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6290717720985413})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6591877937316895})
store['active_learning_steps'][142]['training']['best_epoch']=2
store['active_learning_steps'][142]['evaluation_metrics']={'accuracy': 0.9009, 'crossentropy': 0.577712060546875}
store['active_learning_steps'][142]['acquisition']={'indices': [24959, 32031, 2067, 48152, 52740], 'labels': [-1, 3, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][143]['training']={}
store['active_learning_steps'][143]['training']['epochs']=[]
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.738704264163971})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6263011693954468})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5814148783683777})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.606010913848877})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6994470357894897})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6757110357284546})
store['active_learning_steps'][143]['training']['best_epoch']=3
store['active_learning_steps'][143]['evaluation_metrics']={'accuracy': 0.9229, 'crossentropy': 0.48955205078125}
store['active_learning_steps'][143]['acquisition']={'indices': [41359, 576, 25738, 46855, 27753], 'labels': [-1, 4, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][144]['training']={}
store['active_learning_steps'][144]['training']['epochs']=[]
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.7452390789985657})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5905821323394775})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5326967239379883})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5997673273086548})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5918929576873779})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6132786870002747})
store['active_learning_steps'][144]['training']['best_epoch']=3
store['active_learning_steps'][144]['evaluation_metrics']={'accuracy': 0.9202, 'crossentropy': 0.512057470703125}
store['active_learning_steps'][144]['acquisition']={'indices': [8663, 1463, 44833, 42707, 43602], 'labels': [3, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][145]['training']={}
store['active_learning_steps'][145]['training']['epochs']=[]
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.6991052031517029})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5965306758880615})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6036629676818848})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5689663887023926})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6605980396270752})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5892041921615601})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.7327243089675903})
store['active_learning_steps'][145]['training']['best_epoch']=4
store['active_learning_steps'][145]['evaluation_metrics']={'accuracy': 0.9207, 'crossentropy': 0.510485986328125}
store['active_learning_steps'][145]['acquisition']={'indices': [43723, 46356, 1946, 5301, 24001], 'labels': [-1, 7, 7, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][146]['training']={}
store['active_learning_steps'][146]['training']['epochs']=[]
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7406798601150513})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6010563373565674})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.680412769317627})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.675667941570282})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7688885927200317})
store['active_learning_steps'][146]['training']['best_epoch']=2
store['active_learning_steps'][146]['evaluation_metrics']={'accuracy': 0.8986, 'crossentropy': 0.57974638671875}
store['active_learning_steps'][146]['acquisition']={'indices': [25305, 12291, 44608, 8438, 55106], 'labels': [-1, -1, 3, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][147]['training']={}
store['active_learning_steps'][147]['training']['epochs']=[]
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7100557088851929})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5593979954719543})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6021488308906555})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5719195604324341})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6014032363891602})
store['active_learning_steps'][147]['training']['best_epoch']=2
store['active_learning_steps'][147]['evaluation_metrics']={'accuracy': 0.906, 'crossentropy': 0.54103076171875}
store['active_learning_steps'][147]['acquisition']={'indices': [41892, 859, 36723, 28315, 13404], 'labels': [-1, -1, 3, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][148]['training']={}
store['active_learning_steps'][148]['training']['epochs']=[]
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7513582706451416})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6424469351768494})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5789968967437744})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6425936222076416})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6676302552223206})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7133398056030273})
store['active_learning_steps'][148]['training']['best_epoch']=3
store['active_learning_steps'][148]['evaluation_metrics']={'accuracy': 0.9221, 'crossentropy': 0.501277734375}
store['active_learning_steps'][148]['acquisition']={'indices': [46662, 28278, 7003, 7479, 31838], 'labels': [-1, 2, 0, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][149]['training']={}
store['active_learning_steps'][149]['training']['epochs']=[]
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7735353708267212})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5683926343917847})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6068354249000549})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5513057708740234})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5883679986000061})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5947585105895996})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6379625797271729})
store['active_learning_steps'][149]['training']['best_epoch']=4
store['active_learning_steps'][149]['evaluation_metrics']={'accuracy': 0.9262, 'crossentropy': 0.489789794921875}
store['active_learning_steps'][149]['acquisition']={'indices': [68, 52697, 56981, 19356, 30496], 'labels': [0, 3, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][150]['training']={}
store['active_learning_steps'][150]['training']['epochs']=[]
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7627711296081543})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.61174476146698})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5308399200439453})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4969411790370941})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5714259147644043})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6000785827636719})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6430913209915161})
store['active_learning_steps'][150]['training']['best_epoch']=4
store['active_learning_steps'][150]['evaluation_metrics']={'accuracy': 0.934, 'crossentropy': 0.45439892578125}
store['active_learning_steps'][150]['acquisition']={'indices': [27968, 16735, 18655, 33835, 18542], 'labels': [9, -1, 6, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][151]['training']={}
store['active_learning_steps'][151]['training']['epochs']=[]
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.7529830932617188})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5874505043029785})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5836287140846252})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7160727977752686})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6244179606437683})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6144496202468872})
store['active_learning_steps'][151]['training']['best_epoch']=3
store['active_learning_steps'][151]['evaluation_metrics']={'accuracy': 0.915, 'crossentropy': 0.50815908203125}
store['active_learning_steps'][151]['acquisition']={'indices': [49707, 53588, 8504, 31592, 55073], 'labels': [4, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][152]['training']={}
store['active_learning_steps'][152]['training']['epochs']=[]
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6816402673721313})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.573697566986084})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5175797939300537})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5912749767303467})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6188712120056152})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6244165897369385})
store['active_learning_steps'][152]['training']['best_epoch']=3
store['active_learning_steps'][152]['evaluation_metrics']={'accuracy': 0.9188, 'crossentropy': 0.4893}
store['active_learning_steps'][152]['acquisition']={'indices': [33779, 51868, 10908, 25835, 32329], 'labels': [6, -1, 4, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][153]['training']={}
store['active_learning_steps'][153]['training']['epochs']=[]
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.749930739402771})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5657374262809753})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6353338360786438})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6248611211776733})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5670291185379028})
store['active_learning_steps'][153]['training']['best_epoch']=2
store['active_learning_steps'][153]['evaluation_metrics']={'accuracy': 0.9058, 'crossentropy': 0.553254931640625}
store['active_learning_steps'][153]['acquisition']={'indices': [26371, 34134, 48553, 41748, 51074], 'labels': [-1, -1, -1, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][154]['training']={}
store['active_learning_steps'][154]['training']['epochs']=[]
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.673442542552948})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5677555799484253})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.552518367767334})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6311638355255127})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5924696922302246})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6233813166618347})
store['active_learning_steps'][154]['training']['best_epoch']=3
store['active_learning_steps'][154]['evaluation_metrics']={'accuracy': 0.9191, 'crossentropy': 0.469864306640625}
store['active_learning_steps'][154]['acquisition']={'indices': [24686, 34674, 12954, 56858, 18289], 'labels': [-1, -1, 2, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][155]['training']={}
store['active_learning_steps'][155]['training']['epochs']=[]
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7130709886550903})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.590172290802002})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6569036245346069})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6490345597267151})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6261252760887146})
store['active_learning_steps'][155]['training']['best_epoch']=2
store['active_learning_steps'][155]['evaluation_metrics']={'accuracy': 0.9045, 'crossentropy': 0.529919921875}
store['active_learning_steps'][155]['acquisition']={'indices': [40210, 27168, 39966, 3870, 52301], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][156]['training']={}
store['active_learning_steps'][156]['training']['epochs']=[]
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7158926725387573})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.539729118347168})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6244561076164246})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6681289672851562})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6963933706283569})
store['active_learning_steps'][156]['training']['best_epoch']=2
store['active_learning_steps'][156]['evaluation_metrics']={'accuracy': 0.91, 'crossentropy': 0.538724365234375}
store['active_learning_steps'][156]['acquisition']={'indices': [13858, 56575, 56820, 19916, 9603], 'labels': [-1, 1, 3, 6, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][157]['training']={}
store['active_learning_steps'][157]['training']['epochs']=[]
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7219992876052856})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6149064302444458})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6265578269958496})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.617922306060791})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6295589208602905})
store['active_learning_steps'][157]['training']['best_epoch']=2
store['active_learning_steps'][157]['evaluation_metrics']={'accuracy': 0.8969, 'crossentropy': 0.56946611328125}
store['active_learning_steps'][157]['acquisition']={'indices': [8639, 58876, 59128, 10806, 28538], 'labels': [-1, 1, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][158]['training']={}
store['active_learning_steps'][158]['training']['epochs']=[]
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6989929676055908})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6180427074432373})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5996854901313782})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6311280727386475})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6713064908981323})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6526908278465271})
store['active_learning_steps'][158]['training']['best_epoch']=3
store['active_learning_steps'][158]['evaluation_metrics']={'accuracy': 0.9157, 'crossentropy': 0.508175830078125}
store['active_learning_steps'][158]['acquisition']={'indices': [41915, 6480, 46931, 44931, 29241], 'labels': [4, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][159]['training']={}
store['active_learning_steps'][159]['training']['epochs']=[]
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7569937705993652})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6107465624809265})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6845256090164185})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6485637426376343})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5930322408676147})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7092658281326294})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6849551796913147})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6803320646286011})
store['active_learning_steps'][159]['training']['best_epoch']=5
store['active_learning_steps'][159]['evaluation_metrics']={'accuracy': 0.9252, 'crossentropy': 0.52834599609375}
store['active_learning_steps'][159]['acquisition']={'indices': [48401, 56697, 41334, 55902, 2745], 'labels': [2, 3, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][160]['training']={}
store['active_learning_steps'][160]['training']['epochs']=[]
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7175319194793701})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5957763195037842})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6173295974731445})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6001035571098328})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5532463788986206})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6181994676589966})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6048941612243652})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.655336320400238})
store['active_learning_steps'][160]['training']['best_epoch']=5
store['active_learning_steps'][160]['evaluation_metrics']={'accuracy': 0.9237, 'crossentropy': 0.525278271484375}
store['active_learning_steps'][160]['acquisition']={'indices': [7022, 6609, 8936, 42136, 3254], 'labels': [1, -1, -1, 0, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][161]['training']={}
store['active_learning_steps'][161]['training']['epochs']=[]
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7315406799316406})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5471477508544922})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.587762713432312})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5739586353302002})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6633957624435425})
store['active_learning_steps'][161]['training']['best_epoch']=2
store['active_learning_steps'][161]['evaluation_metrics']={'accuracy': 0.91, 'crossentropy': 0.531270166015625}
store['active_learning_steps'][161]['acquisition']={'indices': [12890, 12668, 59693, 34848, 59219], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][162]['training']={}
store['active_learning_steps'][162]['training']['epochs']=[]
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6523878574371338})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6234697699546814})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5911495685577393})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5812507271766663})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5799542665481567})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6500942707061768})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.7085533738136292})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6656145453453064})
store['active_learning_steps'][162]['training']['best_epoch']=5
store['active_learning_steps'][162]['evaluation_metrics']={'accuracy': 0.9269, 'crossentropy': 0.521538134765625}
store['active_learning_steps'][162]['acquisition']={'indices': [15047, 9422, 49575, 36021, 24727], 'labels': [6, 0, 0, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][163]['training']={}
store['active_learning_steps'][163]['training']['epochs']=[]
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6959505081176758})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6472911834716797})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5689383745193481})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6277726888656616})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6767649054527283})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6312244534492493})
store['active_learning_steps'][163]['training']['best_epoch']=3
store['active_learning_steps'][163]['evaluation_metrics']={'accuracy': 0.9184, 'crossentropy': 0.511733349609375}
store['active_learning_steps'][163]['acquisition']={'indices': [20250, 49838, 29687, 17820, 31266], 'labels': [-1, -1, -1, 3, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][164]['training']={}
store['active_learning_steps'][164]['training']['epochs']=[]
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7246338725090027})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.607869565486908})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5620396733283997})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5739575624465942})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6390498876571655})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6077554225921631})
store['active_learning_steps'][164]['training']['best_epoch']=3
store['active_learning_steps'][164]['evaluation_metrics']={'accuracy': 0.908, 'crossentropy': 0.533849755859375}
store['active_learning_steps'][164]['acquisition']={'indices': [37779, 57819, 32187, 22960, 14170], 'labels': [-1, 4, 1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][165]['training']={}
store['active_learning_steps'][165]['training']['epochs']=[]
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.709561824798584})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6025646924972534})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6152977347373962})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.631069004535675})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6110011339187622})
store['active_learning_steps'][165]['training']['best_epoch']=2
store['active_learning_steps'][165]['evaluation_metrics']={'accuracy': 0.8999, 'crossentropy': 0.5434294921875}
store['active_learning_steps'][165]['acquisition']={'indices': [38082, 13404, 17305, 25165, 36795], 'labels': [-1, 5, 1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][166]['training']={}
store['active_learning_steps'][166]['training']['epochs']=[]
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7456119060516357})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5736215114593506})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5904829502105713})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5918182134628296})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5570882558822632})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6063286066055298})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.640520453453064})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5748304128646851})
store['active_learning_steps'][166]['training']['best_epoch']=5
store['active_learning_steps'][166]['evaluation_metrics']={'accuracy': 0.9252, 'crossentropy': 0.489901416015625}
store['active_learning_steps'][166]['acquisition']={'indices': [31632, 22943, 41071, 27826, 49448], 'labels': [4, -1, 3, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][167]['training']={}
store['active_learning_steps'][167]['training']['epochs']=[]
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7274566292762756})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6137647032737732})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5843256711959839})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6321889162063599})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6741806268692017})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6647894978523254})
store['active_learning_steps'][167]['training']['best_epoch']=3
store['active_learning_steps'][167]['evaluation_metrics']={'accuracy': 0.9204, 'crossentropy': 0.504547119140625}
store['active_learning_steps'][167]['acquisition']={'indices': [826, 39218, 54742, 18236, 36035], 'labels': [9, -1, -1, 2, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][168]['training']={}
store['active_learning_steps'][168]['training']['epochs']=[]
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.74427330493927})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.608167290687561})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5841279625892639})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6838721036911011})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6086000204086304})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.616205096244812})
store['active_learning_steps'][168]['training']['best_epoch']=3
store['active_learning_steps'][168]['evaluation_metrics']={'accuracy': 0.9138, 'crossentropy': 0.518049169921875}
store['active_learning_steps'][168]['acquisition']={'indices': [54281, 26982, 22670, 11945, 36721], 'labels': [-1, 7, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][169]['training']={}
store['active_learning_steps'][169]['training']['epochs']=[]
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7652658224105835})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6390039324760437})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6114640235900879})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.597939133644104})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.610180675983429})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6308637857437134})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6329187154769897})
store['active_learning_steps'][169]['training']['best_epoch']=4
store['active_learning_steps'][169]['evaluation_metrics']={'accuracy': 0.9227, 'crossentropy': 0.48223603515625}
store['active_learning_steps'][169]['acquisition']={'indices': [53349, 43016, 26152, 42150, 8017], 'labels': [9, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][170]['training']={}
store['active_learning_steps'][170]['training']['epochs']=[]
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6505506634712219})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5213941335678101})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4973313808441162})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5086270570755005})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5354154109954834})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6056400537490845})
store['active_learning_steps'][170]['training']['best_epoch']=3
store['active_learning_steps'][170]['evaluation_metrics']={'accuracy': 0.9229, 'crossentropy': 0.462210009765625}
store['active_learning_steps'][170]['acquisition']={'indices': [24250, 7636, 32139, 5602, 29036], 'labels': [-1, 8, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][171]['training']={}
store['active_learning_steps'][171]['training']['epochs']=[]
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6622583866119385})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5439654588699341})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5030245780944824})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5590291619300842})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5367847084999084})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6099703311920166})
store['active_learning_steps'][171]['training']['best_epoch']=3
store['active_learning_steps'][171]['evaluation_metrics']={'accuracy': 0.9223, 'crossentropy': 0.477689111328125}
store['active_learning_steps'][171]['acquisition']={'indices': [17365, 33295, 10534, 5351, 21062], 'labels': [0, -1, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][172]['training']={}
store['active_learning_steps'][172]['training']['epochs']=[]
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.666954517364502})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5339869856834412})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6285938024520874})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.569037675857544})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5509058833122253})
store['active_learning_steps'][172]['training']['best_epoch']=2
store['active_learning_steps'][172]['evaluation_metrics']={'accuracy': 0.9185, 'crossentropy': 0.4747396484375}
store['active_learning_steps'][172]['acquisition']={'indices': [40952, 39764, 45099, 4501, 19847], 'labels': [-1, -1, 2, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][173]['training']={}
store['active_learning_steps'][173]['training']['epochs']=[]
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6662373542785645})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6630975604057312})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6325867176055908})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5034791231155396})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.571942925453186})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5812985897064209})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.630333662033081})
store['active_learning_steps'][173]['training']['best_epoch']=4
store['active_learning_steps'][173]['evaluation_metrics']={'accuracy': 0.9249, 'crossentropy': 0.47384296875}
store['active_learning_steps'][173]['acquisition']={'indices': [7605, 5308, 57877, 57326, 5180], 'labels': [7, -1, 3, 0, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][174]['training']={}
store['active_learning_steps'][174]['training']['epochs']=[]
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.7341557741165161})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5954060554504395})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5803521871566772})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5612742900848389})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.569198727607727})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5904151201248169})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.643555760383606})
store['active_learning_steps'][174]['training']['best_epoch']=4
store['active_learning_steps'][174]['evaluation_metrics']={'accuracy': 0.9281, 'crossentropy': 0.489590771484375}
