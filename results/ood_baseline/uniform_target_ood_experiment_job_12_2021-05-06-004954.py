store = {}
store['timestamp']=1620258594
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=12']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=12
store['worker_id']=12
store['num_workers']=40
store['config']={'seed': 15, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 50, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.22647762298584})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.7895848751068115})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.876115322113037})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.3368749618530273})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6733, 'crossentropy': 2.1569302734375}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 52228], ['id', 2521], ['id', 33387], ['id', 57018], ['id', 54654]], 'labels': [0, 9, 8, 9, 8], 'scores': [0.8684996366500854, 0.7772238254547119, 0.7204044461250305, 0.7946926951408386, 0.7910852432250977]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.1484761238098145})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.823288917541504})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.841794967651367})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 3.4457602500915527})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6905, 'crossentropy': 1.9977734375}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 35511], ['id', 17137], ['id', 45207], ['id', 2250], ['id', 35606]], 'labels': [3, 2, 8, 5, 2], 'scores': [0.5560653805732727, 1.0828703045845032, 0.9866989254951477, 0.7692327499389648, 0.8144547343254089]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.230320930480957})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.4919838905334473})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.7019906044006348})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.633859157562256})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6882, 'crossentropy': 1.9125228515625}
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 57706], ['ood', 28853], ['id', 46406], ['id', 7904], ['id', 15423]], 'labels': [0, 1, 3, 9, 1], 'scores': [0.41442203521728516, 0.5386412143707275, 0.8374451398849487, 0.8669400811195374, 0.7881371974945068]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.4940123558044434})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.799092411994934})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.4344592094421387})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.6197080612182617})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7384, 'crossentropy': 1.38915185546875}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 19108], ['id', 30164], ['id', 2457], ['id', 39595], ['id', 31491]], 'labels': [5, 4, 2, 3, 6], 'scores': [0.584747850894928, 0.6245442628860474, 0.4680468440055847, 0.49679625034332275, 0.6061341762542725]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.4520260095596313})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.7437188625335693})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.188769817352295})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 2.085392713546753})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7477, 'crossentropy': 1.399666796875}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 35963], ['id', 10103], ['ood', 5349], ['id', 39016], ['id', 57595]], 'labels': [0, 4, 7, 9, 0], 'scores': [0.6342930197715759, 0.6028143167495728, 0.5772485733032227, 0.9402582049369812, 1.0444620847702026]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.0709924697875977})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.300048828125})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.2161715030670166})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.4175910949707031})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8022, 'crossentropy': 0.987165625}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 17084], ['id', 14887], ['id', 2881], ['id', 24650], ['id', 22404]], 'labels': [8, 5, 7, 5, 3], 'scores': [0.46092796325683594, 0.6543598175048828, 0.7117885947227478, 0.7304490804672241, 0.6522608995437622]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.1321418285369873})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.0816752910614014})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.1439766883850098})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.5317949056625366})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.3528516292572021})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8188, 'crossentropy': 1.02158154296875}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 20486], ['id', 42398], ['id', 15462], ['id', 28102], ['id', 12508]], 'labels': [6, 3, 5, 0, 1], 'scores': [0.9010294675827026, 0.5180275440216064, 0.7765887379646301, 0.790663480758667, 0.8129000663757324]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.0918099880218506})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.1712162494659424})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.1403496265411377})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.2576450109481812})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8156, 'crossentropy': 0.92690986328125}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 46674], ['id', 33246], ['id', 49470], ['id', 37969], ['id', 41000]], 'labels': [3, 9, 5, 2, 5], 'scores': [0.6313278079032898, 0.3914657235145569, 0.5792190432548523, 0.5358936786651611, 0.534691572189331]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.0540287494659424})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.128840684890747})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.1470656394958496})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.1182568073272705})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8083, 'crossentropy': 0.9178509765625}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 53473], ['id', 41527], ['id', 56975], ['id', 39942], ['id', 24853]], 'labels': [2, 7, 3, 9, 2], 'scores': [0.5596256852149963, 0.6766821146011353, 0.601277232170105, 0.5648982524871826, 0.6714766621589661]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.038773536682129})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.0758821964263916})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.051690697669983})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.2045847177505493})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8151, 'crossentropy': 0.92693984375}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 58503], ['id', 9867], ['id', 53990], ['id', 53232], ['id', 43807]], 'labels': [3, 4, 4, 7, 6], 'scores': [0.7329320907592773, 0.5905278921127319, 0.5064339637756348, 0.7631599307060242, 0.3580082654953003]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9351494312286377})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8787168264389038})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0537596940994263})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.1052742004394531})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.244217872619629})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8582, 'crossentropy': 0.780088330078125}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 35652], ['id', 14811], ['id', 14975], ['id', 49517], ['id', 1812]], 'labels': [2, 4, 8, 6, 4], 'scores': [0.6056874394416809, 0.7279313802719116, 0.723659336566925, 0.8959864377975464, 0.661302924156189]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9545387029647827})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8359808921813965})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9049334526062012})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9024513959884644})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9409557580947876})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8809, 'crossentropy': 0.705278759765625}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 5069], ['id', 7033], ['id', 26733], ['id', 18910], ['id', 36908]], 'labels': [4, 7, 2, 7, 1], 'scores': [0.4781900644302368, 0.7790266275405884, 0.957003116607666, 0.707493007183075, 0.6566917300224304]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7934306263923645})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8636152744293213})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9242079854011536})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8865782022476196})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8678, 'crossentropy': 0.726673779296875}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 32519], ['id', 12345], ['id', 35654], ['id', 2288], ['id', 11030]], 'labels': [5, 3, 1, 2, 2], 'scores': [0.4935201406478882, 0.7678192853927612, 0.6020519733428955, 0.5884836912155151, 0.6288046836853027]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.805644154548645})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7866072654724121})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8308963775634766})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9278448224067688})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8790961503982544})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8689, 'crossentropy': 0.691127685546875}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 57319], ['id', 29365], ['id', 14791], ['id', 17784], ['id', 18473]], 'labels': [2, 8, 8, 8, 4], 'scores': [0.49752962589263916, 0.5932769775390625, 0.6118694543838501, 0.5473941564559937, 0.8298607468605042]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9513761401176453})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9241892099380493})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.95952308177948})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9893170595169067})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0425660610198975})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8549, 'crossentropy': 0.800588330078125}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 37016], ['id', 15892], ['id', 36078], ['ood', 27721], ['id', 58086]], 'labels': [5, 5, 3, 3, 3], 'scores': [0.7177554368972778, 0.6630834937095642, 0.6991852521896362, 0.35475659370422363, 0.5833458304405212]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9460306167602539})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7288352251052856})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7999024391174316})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7871524095535278})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8785256147384644})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8855, 'crossentropy': 0.671823583984375}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 38319], ['id', 21395], ['id', 30870], ['id', 25960], ['id', 44384]], 'labels': [2, 8, 8, 4, 9], 'scores': [0.5547225475311279, 0.7399449944496155, 0.587448000907898, 0.68207186460495, 0.49029940366744995]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8203202486038208})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6984423398971558})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7090222835540771})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7084472179412842})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8090357780456543})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8864, 'crossentropy': 0.626146630859375}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 53029], ['id', 32106], ['id', 16084], ['id', 17558], ['id', 37702]], 'labels': [2, 3, 5, 5, 9], 'scores': [0.46474409103393555, 0.5708390474319458, 0.732915461063385, 0.5230433940887451, 0.6830836534500122]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7584927082061768})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7129305601119995})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6678150296211243})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7823144197463989})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7589612007141113})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7387816905975342})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9066, 'crossentropy': 0.576435791015625}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 40084], ['id', 40087], ['id', 50052], ['id', 9263], ['id', 14286]], 'labels': [2, 3, 2, 7, 3], 'scores': [0.8029540777206421, 0.6637422442436218, 0.861016035079956, 0.5868910551071167, 0.7468242645263672]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8635588884353638})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7527163028717041})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7393227815628052})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.726371169090271})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7190743684768677})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7946333885192871})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.794296383857727})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8646788001060486})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9104, 'crossentropy': 0.58518935546875}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 22042], ['ood', 7402], ['id', 6582], ['id', 2000], ['id', 20287]], 'labels': [5, 5, 8, 5, 4], 'scores': [0.7662769854068756, 0.5175168514251709, 0.6999812722206116, 0.8330094218254089, 0.8315601944923401]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9509291648864746})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5791196227073669})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6644850969314575})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5986469388008118})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6434115171432495})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9082, 'crossentropy': 0.54861181640625}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 46242], ['id', 6327], ['id', 57523], ['id', 1674], ['id', 14705]], 'labels': [3, 2, 3, 9, 0], 'scores': [0.7076971530914307, 0.7641939520835876, 0.7468470335006714, 0.8174047470092773, 0.610320508480072]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8748332262039185})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6633108258247375})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6944539546966553})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6985806226730347})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7126387357711792})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9055, 'crossentropy': 0.56619111328125}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 3010], ['id', 49908], ['id', 27608], ['id', 26443], ['id', 17512]], 'labels': [7, 2, 8, 8, 8], 'scores': [0.7930833101272583, 0.5755364894866943, 0.6781408786773682, 0.5907096862792969, 0.7093251943588257]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8890937566757202})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6299603581428528})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5773163437843323})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5998750925064087})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5663154721260071})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6275047063827515})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6377537846565247})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5985554456710815})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9187, 'crossentropy': 0.5296703125}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 37676], ['id', 35611], ['id', 24391], ['id', 34740], ['id', 34811]], 'labels': [6, 5, 4, 3, 5], 'scores': [0.7553840279579163, 0.8510620594024658, 0.7771411538124084, 0.771823525428772, 0.7622054815292358]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8918591737747192})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6810727119445801})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5956764221191406})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6787473559379578})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.572900652885437})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6850358247756958})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7872951030731201})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6986223459243774})
store['active_learning_steps'][22]['training']['best_epoch']=5
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9174, 'crossentropy': 0.5400390625}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 6272], ['id', 35303], ['id', 12069], ['id', 41453], ['id', 29472]], 'labels': [9, 1, 9, 3, 9], 'scores': [0.9576941132545471, 0.6034291982650757, 0.7169510722160339, 0.7791132926940918, 0.6896710991859436]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8787899017333984})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5981124639511108})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6070271134376526})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6027126908302307})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5403430461883545})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6116099953651428})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.584682822227478})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6168742179870605})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.928, 'crossentropy': 0.475361669921875}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 20641], ['id', 13881], ['id', 44737], ['id', 36010], ['id', 51004]], 'labels': [9, 6, 7, 8, 7], 'scores': [0.7655083537101746, 0.7042102217674255, 0.9107010364532471, 0.8466132879257202, 0.6228678822517395]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9312996864318848})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5482006072998047})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5791394710540771})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5410423278808594})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5559795498847961})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5929802656173706})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6094058752059937})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9253, 'crossentropy': 0.483412744140625}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 55496], ['id', 49503], ['ood', 25515], ['id', 31881], ['id', 4058]], 'labels': [9, 5, 8, 8, 8], 'scores': [0.8507257103919983, 0.5222947299480438, 0.6222354769706726, 0.8653401136398315, 0.849256694316864]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9064781069755554})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6391756534576416})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.528659999370575})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5846878290176392})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6227339506149292})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6633839011192322})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9276, 'crossentropy': 0.46642080078125}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 11342], ['id', 13827], ['id', 59830], ['id', 57541], ['id', 53872]], 'labels': [1, 3, 7, 7, 8], 'scores': [0.46983784437179565, 0.7293247580528259, 0.5529975295066833, 0.7474486231803894, 0.7777409553527832]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8919481039047241})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.548431396484375})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5108345746994019})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5378569960594177})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5168583989143372})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.559627890586853})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9245, 'crossentropy': 0.48255498046875}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 35882], ['id', 46709], ['id', 4986], ['id', 42863], ['id', 11295]], 'labels': [2, 3, 2, 5, 0], 'scores': [0.6511551737785339, 0.5363271832466125, 0.5233566164970398, 0.7613742351531982, 0.5285829305648804]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.870904803276062})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6284003257751465})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5333248376846313})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.542686402797699})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5675085783004761})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5925235152244568})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9315, 'crossentropy': 0.441322216796875}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 28556], ['id', 24589], ['id', 55678], ['id', 51769], ['id', 25120]], 'labels': [4, 8, 2, 8, 8], 'scores': [0.6083300113677979, 0.7204025983810425, 0.6897405982017517, 0.5520527362823486, 0.5382511019706726]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9436975121498108})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5661754608154297})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5450100898742676})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5490292906761169})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5431499481201172})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5234410762786865})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5046614408493042})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5216965079307556})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5626792907714844})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6026920080184937})
store['active_learning_steps'][28]['training']['best_epoch']=7
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9415, 'crossentropy': 0.439538037109375}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 59574], ['ood', 32120], ['id', 14687], ['id', 137], ['id', 30584]], 'labels': [5, 0, 9, 8, 8], 'scores': [0.7602907121181488, 0.5384014844894409, 0.6758479475975037, 0.5930687785148621, 0.7935537695884705]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9490304589271545})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5464869737625122})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5665863156318665})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4803246259689331})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.439064085483551})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5179503560066223})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.49637874960899353})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6162996292114258})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9398, 'crossentropy': 0.3924100830078125}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 30838], ['id', 17450], ['id', 11457], ['id', 37249], ['id', 46584]], 'labels': [9, 4, 8, 5, 8], 'scores': [0.6915761232376099, 0.7037018537521362, 0.547741174697876, 0.6321664750576019, 0.5650209188461304]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.0443181991577148})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.605789065361023})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5642777681350708})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5720301270484924})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5475267171859741})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5521066188812256})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5306565761566162})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.595751166343689})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5657929182052612})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5703080892562866})
store['active_learning_steps'][30]['training']['best_epoch']=7
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9381, 'crossentropy': 0.437383056640625}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 26850], ['id', 7233], ['id', 34504], ['id', 11747], ['id', 31200]], 'labels': [2, 9, 9, 3, 9], 'scores': [0.9036745429039001, 0.7296668887138367, 0.8005656003952026, 0.5839509665966034, 0.8097776174545288]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.1012310981750488})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6494255661964417})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5182138085365295})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.447298139333725})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4727919101715088})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.40543872117996216})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4961136281490326})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5144037008285522})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.48832759261131287})
store['active_learning_steps'][31]['training']['best_epoch']=6
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9521, 'crossentropy': 0.37191083984375}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 51158], ['id', 52727], ['id', 45491], ['id', 5013], ['id', 4165]], 'labels': [8, 4, 5, 2, 2], 'scores': [0.7626287341117859, 0.8087019324302673, 0.8235888481140137, 0.7111839056015015, 0.7869017124176025]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.0665392875671387})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6041338443756104})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5324985980987549})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5104846358299255})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.505811333656311})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4795833230018616})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5659609436988831})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5135080218315125})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4903291165828705})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9421, 'crossentropy': 0.3989916259765625}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 42078], ['id', 134], ['id', 57421], ['id', 27153], ['id', 995]], 'labels': [4, 1, 9, 0, 7], 'scores': [0.9391783475875854, 0.8564190864562988, 0.48718470335006714, 0.8956589698791504, 0.6246125102043152]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9626548886299133})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5984311699867249})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.487534761428833})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.43561241030693054})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4335220456123352})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4785442352294922})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.48983532190322876})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5728820562362671})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9497, 'crossentropy': 0.3706731201171875}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 24944], ['id', 28368], ['id', 27793], ['id', 27780], ['id', 13614]], 'labels': [6, 9, 1, 9, 6], 'scores': [0.5272580981254578, 0.8527291417121887, 0.8384664058685303, 0.7315388321876526, 0.8144464492797852]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.0676836967468262})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5876450538635254})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4884878396987915})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4529426693916321})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.44636738300323486})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4363887310028076})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4369683265686035})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4233686327934265})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4599629044532776})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.49333855509757996})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5304028391838074})
store['active_learning_steps'][34]['training']['best_epoch']=8
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9515, 'crossentropy': 0.376104052734375}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 23016], ['id', 37254], ['id', 59940], ['id', 17371], ['id', 30184]], 'labels': [9, 6, 0, 3, 9], 'scores': [0.6823175549507141, 0.7024285793304443, 0.673956573009491, 0.9601844549179077, 0.9154589772224426]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.1696062088012695})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5192679166793823})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5224325656890869})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.46333742141723633})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4323005974292755})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4336130619049072})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.43716898560523987})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.40922456979751587})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.46614333987236023})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.46165740489959717})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4253987669944763})
store['active_learning_steps'][35]['training']['best_epoch']=8
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9542, 'crossentropy': 0.371540625}
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 35589], ['id', 17756], ['id', 26101], ['id', 9687], ['id', 12196]], 'labels': [5, 8, 6, 0, 2], 'scores': [0.4865065813064575, 0.7039881348609924, 0.5900941491127014, 0.6549904346466064, 1.0249838829040527]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.01067316532135})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.509458601474762})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5446333885192871})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4757666289806366})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.44007501006126404})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4211745858192444})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.44278961420059204})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.41246846318244934})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.440430223941803})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4538562297821045})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.47177979350090027})
store['active_learning_steps'][36]['training']['best_epoch']=8
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9556, 'crossentropy': 0.3760620849609375}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 23870], ['id', 48885], ['id', 21990], ['id', 20093], ['id', 31794]], 'labels': [5, 4, 1, 5, 2], 'scores': [1.0974167585372925, 0.38108283281326294, 0.7662404775619507, 0.7246122360229492, 0.5842823684215546]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 1.0270545482635498})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5223979949951172})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4301484227180481})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.40667253732681274})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.36267462372779846})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38158756494522095})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.40240955352783203})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.36666423082351685})
store['active_learning_steps'][37]['training']['best_epoch']=5
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.956, 'crossentropy': 0.373645263671875}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 47787], ['id', 30811], ['id', 31988], ['id', 40380], ['id', 11621]], 'labels': [2, 2, 3, 1, 2], 'scores': [0.45662373304367065, 0.7509649395942688, 0.8279098272323608, 0.3299320340156555, 0.6695352792739868]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8065040111541748})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.48302823305130005})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4371664822101593})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3615422248840332})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3749556243419647})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.39258819818496704})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35690566897392273})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3551587164402008})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4068026542663574})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.45695269107818604})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.42108529806137085})
store['active_learning_steps'][38]['training']['best_epoch']=8
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9532, 'crossentropy': 0.3519482666015625}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 49499], ['id', 13253], ['id', 44432], ['id', 37078], ['id', 13942]], 'labels': [1, 5, 1, 8, 4], 'scores': [0.6704756021499634, 0.8477755188941956, 0.7113399505615234, 0.9718429446220398, 0.714921236038208]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.1193008422851562})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5314052104949951})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4334184229373932})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4517672061920166})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36659613251686096})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3831245005130768})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.40480920672416687})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4540477395057678})
store['active_learning_steps'][39]['training']['best_epoch']=5
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9531, 'crossentropy': 0.3582847412109375}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 11296], ['id', 53316], ['id', 27122], ['id', 49541], ['id', 1127]], 'labels': [3, 5, 2, 9, 7], 'scores': [0.8276883363723755, 0.8987005352973938, 0.5295997262001038, 0.688004195690155, 0.7807678580284119]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.0975993871688843})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5609131455421448})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.481967031955719})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4062851071357727})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.41111546754837036})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4899798631668091})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4200708866119385})
store['active_learning_steps'][40]['training']['best_epoch']=4
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9487, 'crossentropy': 0.367660302734375}
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 44538], ['id', 52886], ['id', 22523], ['id', 7954], ['id', 15826]], 'labels': [5, 7, 9, 0, 6], 'scores': [0.6799374222755432, 0.6274381875991821, 0.39875176548957825, 0.684354305267334, 0.5593036711215973]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.0052504539489746})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.515977144241333})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3962184190750122})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.36240094900131226})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3854469358921051})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.361866295337677})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3295375108718872})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3353498578071594})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3751984238624573})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3515744209289551})
store['active_learning_steps'][41]['training']['best_epoch']=7
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9629, 'crossentropy': 0.29959267578125}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 43169], ['id', 42799], ['id', 39778], ['id', 35864], ['id', 4955]], 'labels': [0, 2, 8, 5, 2], 'scores': [0.5618734955787659, 0.8344531655311584, 1.1683483719825745, 1.037385106086731, 0.7695747017860413]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.0564806461334229})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5831626653671265})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.46376657485961914})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4682096838951111})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4268650412559509})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4161815941333771})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.40408676862716675})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.40646129846572876})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.45168536901474})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4351036846637726})
store['active_learning_steps'][42]['training']['best_epoch']=7
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9592, 'crossentropy': 0.3453943603515625}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 45784], ['id', 27598], ['id', 27514], ['id', 16756], ['id', 17190]], 'labels': [9, 2, 4, 7, 9], 'scores': [0.843990683555603, 0.8004998862743378, 0.9290444254875183, 0.964020848274231, 0.7481780648231506]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.0157763957977295})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5289403200149536})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.39629241824150085})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.40675950050354004})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.45802223682403564})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.41652730107307434})
store['active_learning_steps'][43]['training']['best_epoch']=3
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9496, 'crossentropy': 0.36170908203125}
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 1352], ['id', 22481], ['id', 39668], ['id', 19846], ['ood', 11921]], 'labels': [9, 7, 8, 5, 9], 'scores': [0.6837751865386963, 0.67127925157547, 0.5872052311897278, 0.5269833207130432, 0.32881736755371094]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.099153995513916})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5755398869514465})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4719052314758301})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.41393381357192993})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.44533973932266235})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4167689085006714})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.38287943601608276})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.40082138776779175})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.419511079788208})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3897009789943695})
store['active_learning_steps'][44]['training']['best_epoch']=7
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9527, 'crossentropy': 0.3280722412109375}
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 17486], ['id', 23039], ['id', 2622], ['id', 30429], ['id', 37352]], 'labels': [7, 2, 5, 2, 9], 'scores': [0.6711790561676025, 0.39936280250549316, 0.6019071340560913, 0.6111185550689697, 0.87679722905159]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9720430374145508})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5349998474121094})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4738023579120636})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4386383891105652})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4081431031227112})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.40281349420547485})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.436694860458374})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4307818114757538})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4310113191604614})
store['active_learning_steps'][45]['training']['best_epoch']=6
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9561, 'crossentropy': 0.3471914306640625}
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 47494], ['id', 14062], ['id', 51650], ['id', 38557], ['id', 12268]], 'labels': [5, 8, 7, 7, 8], 'scores': [0.3687468469142914, 0.7434201240539551, 0.4953465461730957, 0.546495795249939, 0.8042758703231812]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.0720391273498535})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.49513423442840576})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4041627049446106})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3689265549182892})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3600700795650482})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3844578266143799})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3398708999156952})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3632194399833679})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3406819999217987})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.38047611713409424})
store['active_learning_steps'][46]['training']['best_epoch']=7
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9568, 'crossentropy': 0.32424990234375}
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 42828], ['id', 9450], ['id', 34414], ['id', 43906], ['id', 13969]], 'labels': [7, 5, 8, 4, 3], 'scores': [0.7090467214584351, 0.6210722327232361, 0.574648916721344, 0.7799880504608154, 0.8353897929191589]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.1448776721954346})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5596059560775757})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.42928335070610046})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.40466204285621643})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.364194393157959})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.41183018684387207})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.40025222301483154})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.40108293294906616})
store['active_learning_steps'][47]['training']['best_epoch']=5
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9586, 'crossentropy': 0.3449291259765625}
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 50317], ['id', 32509], ['id', 12497], ['id', 39329], ['id', 13428]], 'labels': [3, 8, 0, 3, 9], 'scores': [0.8868427872657776, 0.3588806390762329, 0.41453224420547485, 0.723040759563446, 0.7040784358978271]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.1628494262695312})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.546101987361908})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4374440312385559})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4001355469226837})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32459884881973267})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3485296070575714})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31975603103637695})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.378362774848938})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.31292372941970825})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33012253046035767})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3509330153465271})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3560037612915039})
store['active_learning_steps'][48]['training']['best_epoch']=9
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9622, 'crossentropy': 0.30660244140625}
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 5170], ['id', 11016], ['id', 36687], ['id', 22320], ['id', 40646]], 'labels': [8, 4, 1, 8, 8], 'scores': [0.6709336638450623, 0.4793785810470581, 0.48198312520980835, 0.9150984883308411, 0.6206849217414856]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.2377957105636597})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6035401225090027})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4542696475982666})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4180818796157837})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4147195816040039})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3535870909690857})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3576231896877289})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3920644521713257})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.38370662927627563})
store['active_learning_steps'][49]['training']['best_epoch']=6
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9598, 'crossentropy': 0.3267913818359375}
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 8093], ['id', 45443], ['id', 25386], ['id', 27602], ['id', 2580]], 'labels': [0, 5, 0, 5, 3], 'scores': [0.7758476734161377, 0.7710094451904297, 0.8035536408424377, 0.5155380368232727, 0.5815894901752472]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.110480785369873})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5919021368026733})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4953424334526062})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4186437129974365})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.39032912254333496})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3724684715270996})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.35138168931007385})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.40780875086784363})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4365663230419159})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.46548575162887573})
store['active_learning_steps'][50]['training']['best_epoch']=7
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9625, 'crossentropy': 0.309404931640625}
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 935], ['id', 27994], ['id', 4590], ['id', 50607], ['id', 44287]], 'labels': [8, 8, 5, 8, 6], 'scores': [0.7249244451522827, 0.7400540113449097, 0.8605712056159973, 0.5765699744224548, 0.7246242165565491]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.1893551349639893})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6823863983154297})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.45285046100616455})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.40230095386505127})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3790680170059204})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4223968982696533})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3898508846759796})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.39390799403190613})
store['active_learning_steps'][51]['training']['best_epoch']=5
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9567, 'crossentropy': 0.33769658203125}
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 148], ['id', 45972], ['id', 37247], ['id', 44149], ['id', 33812]], 'labels': [7, 2, 9, 2, 6], 'scores': [0.5542399287223816, 0.49280744791030884, 0.668627917766571, 0.6362793445587158, 0.9659237861633301]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.0779106616973877})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5378100872039795})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.40941911935806274})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36230409145355225})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.37479621171951294})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32647600769996643})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35955220460891724})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3685349225997925})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33380240201950073})
store['active_learning_steps'][52]['training']['best_epoch']=6
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9639, 'crossentropy': 0.290904443359375}
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 42428], ['id', 3810], ['id', 11858], ['id', 52392], ['id', 37122]], 'labels': [5, 3, 8, 1, 8], 'scores': [0.7569717168807983, 0.9144546389579773, 0.6124142408370972, 0.417110800743103, 0.6829116940498352]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.2612082958221436})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6446022987365723})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5571887493133545})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4384932518005371})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.42912012338638306})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.35905396938323975})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36765921115875244})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.40020322799682617})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.362521231174469})
store['active_learning_steps'][53]['training']['best_epoch']=6
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9585, 'crossentropy': 0.3238438232421875}
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 48006], ['id', 51863], ['id', 54582], ['id', 30545], ['id', 7979]], 'labels': [6, 9, 4, 8, 8], 'scores': [0.782665878534317, 0.7832916378974915, 0.5058302581310272, 0.7923699617385864, 0.6016765236854553]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.2740774154663086})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6082812547683716})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4880586266517639})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4159315228462219})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39297592639923096})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3384356200695038})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3552476167678833})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3654887080192566})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4007989764213562})
store['active_learning_steps'][54]['training']['best_epoch']=6
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9604, 'crossentropy': 0.3022426513671875}
store['active_learning_steps'][54]['acquisition']={'indices': [['id', 33752], ['id', 59339], ['id', 26852], ['id', 14757], ['id', 40240]], 'labels': [1, 1, 8, 7, 0], 'scores': [0.8832082748413086, 0.6784614324569702, 0.44326871633529663, 0.4170374572277069, 0.5802954435348511]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.2189218997955322})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6322833299636841})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.47750306129455566})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3873881697654724})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3705204725265503})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.347840815782547})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3586968779563904})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35402536392211914})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.38126158714294434})
store['active_learning_steps'][55]['training']['best_epoch']=6
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9605, 'crossentropy': 0.3110820556640625}
store['active_learning_steps'][55]['acquisition']={'indices': [['id', 28374], ['id', 42221], ['id', 56480], ['id', 47140], ['id', 58344]], 'labels': [3, 5, 9, 3, 9], 'scores': [0.7378450632095337, 0.6970899701118469, 0.659182071685791, 0.86114501953125, 0.4749292731285095]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0785841941833496})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5440486073493958})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.41639244556427})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.37833037972450256})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.36728447675704956})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36116480827331543})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3424326181411743})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3524947166442871})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.378314733505249})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3115459084510803})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.40080636739730835})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3620213270187378})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.38595810532569885})
store['active_learning_steps'][56]['training']['best_epoch']=10
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9684, 'crossentropy': 0.2869359375}
store['active_learning_steps'][56]['acquisition']={'indices': [['ood', 58633], ['id', 12971], ['id', 13242], ['id', 31514], ['id', 15209]], 'labels': [9, 1, 3, 4, 7], 'scores': [0.39098286628723145, 0.5247577428817749, 0.8197687864303589, 0.5399183034896851, 0.550881564617157]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.1302542686462402})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5256965160369873})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4447830617427826})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36161375045776367})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36448121070861816})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34543097019195557})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35924339294433594})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34777265787124634})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3569334149360657})
store['active_learning_steps'][57]['training']['best_epoch']=6
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9605, 'crossentropy': 0.319215087890625}
store['active_learning_steps'][57]['acquisition']={'indices': [['id', 25640], ['id', 41604], ['id', 58995], ['id', 15855], ['id', 31706]], 'labels': [9, 7, 1, 5, 8], 'scores': [0.7360799312591553, 0.4610121250152588, 0.5557176470756531, 0.7903330326080322, 0.8216238021850586]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.005159616470337})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5283880829811096})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.42049741744995117})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.38324928283691406})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3376602530479431})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.33742791414260864})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34175166487693787})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3699610233306885})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3384622633457184})
store['active_learning_steps'][58]['training']['best_epoch']=6
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9636, 'crossentropy': 0.282612939453125}
store['active_learning_steps'][58]['acquisition']={'indices': [['id', 21726], ['id', 40407], ['id', 40022], ['id', 50413], ['id', 1758]], 'labels': [3, 6, 8, 8, 8], 'scores': [0.6076881289482117, 0.4774506688117981, 0.6593343019485474, 0.5011507272720337, 0.5706567764282227]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0917885303497314})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5857205390930176})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4157859683036804})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3629690110683441})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3378852605819702})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37694454193115234})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.325499951839447})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29255926609039307})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3058537244796753})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2883716821670532})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3040492534637451})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3111678659915924})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3313935399055481})
store['active_learning_steps'][59]['training']['best_epoch']=10
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9686, 'crossentropy': 0.2793582763671875}
store['active_learning_steps'][59]['acquisition']={'indices': [['id', 59321], ['id', 8606], ['id', 49146], ['ood', 5194], ['id', 6044]], 'labels': [4, 3, 4, 2, 2], 'scores': [0.6440799236297607, 0.45531895756721497, 0.637898862361908, 0.3980358839035034, 0.5922669172286987]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.1846989393234253})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5413403511047363})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.42808011174201965})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.39731326699256897})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34493398666381836})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35648244619369507})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3329237699508667})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3222707509994507})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4056066870689392})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3354729115962982})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34563297033309937})
store['active_learning_steps'][60]['training']['best_epoch']=8
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.966, 'crossentropy': 0.2891208740234375}
store['active_learning_steps'][60]['acquisition']={'indices': [['id', 42838], ['id', 37574], ['id', 39208], ['id', 7631], ['id', 50743]], 'labels': [9, 5, 5, 1, 7], 'scores': [0.8035306334495544, 0.9511741697788239, 0.9043298959732056, 0.6010122895240784, 0.9120209813117981]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.215442180633545})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5593059659004211})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4148917496204376})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35744303464889526})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.33290791511535645})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35397955775260925})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3221578001976013})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2993312478065491})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2983759641647339})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33182454109191895})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3259369134902954})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3426928222179413})
store['active_learning_steps'][61]['training']['best_epoch']=9
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9709, 'crossentropy': 0.2605097412109375}
store['active_learning_steps'][61]['acquisition']={'indices': [['id', 24740], ['ood', 9203], ['id', 14715], ['id', 30962], ['id', 19702]], 'labels': [8, 8, 4, 3, 5], 'scores': [1.0194814205169678, 0.4684234857559204, 0.64009690284729, 0.8220857977867126, 0.6534067392349243]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.0907158851623535})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5664217472076416})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4596008062362671})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3720511198043823})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33192211389541626})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33556288480758667})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31898611783981323})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36386698484420776})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3369786739349365})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30540546774864197})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3040609359741211})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32389402389526367})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3484359085559845})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37112265825271606})
store['active_learning_steps'][62]['training']['best_epoch']=11
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9712, 'crossentropy': 0.260493798828125}
store['active_learning_steps'][62]['acquisition']={'indices': [['id', 29141], ['id', 5230], ['id', 8812], ['id', 6291], ['id', 11776]], 'labels': [4, 6, 0, 3, 5], 'scores': [0.737506091594696, 0.47378337383270264, 0.5375320017337799, 0.8965020179748535, 0.7354209125041962]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1200494766235352})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6310667395591736})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35627660155296326})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4100409150123596})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3274846076965332})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29268255829811096})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34949028491973877})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3394406735897064})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.317940890789032})
store['active_learning_steps'][63]['training']['best_epoch']=6
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9682, 'crossentropy': 0.2648312744140625}
store['active_learning_steps'][63]['acquisition']={'indices': [['id', 40654], ['id', 45034], ['id', 15328], ['id', 41204], ['id', 30884]], 'labels': [5, 9, 2, 2, 2], 'scores': [0.8085261583328247, 0.6213108897209167, 0.5745075941085815, 0.4623267650604248, 0.5734965801239014]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8975130915641785})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5540534257888794})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.40192851424217224})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3317791223526001})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33271920680999756})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32258331775665283})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3767482340335846})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32093751430511475})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33419567346572876})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33242255449295044})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34592342376708984})
store['active_learning_steps'][64]['training']['best_epoch']=8
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9692, 'crossentropy': 0.2571311279296875}
store['active_learning_steps'][64]['acquisition']={'indices': [['id', 30493], ['id', 26184], ['id', 11568], ['id', 52294], ['id', 20150]], 'labels': [1, 0, 8, 0, 3], 'scores': [0.8564227223396301, 0.5695093274116516, 0.5259000658988953, 0.7267647385597229, 0.767195999622345]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.082548975944519})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5037825703620911})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.426996648311615})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34006479382514954})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.30409932136535645})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2879829406738281})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3372529149055481})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3376994729042053})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35727658867836})
store['active_learning_steps'][65]['training']['best_epoch']=6
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9677, 'crossentropy': 0.259680517578125}
store['active_learning_steps'][65]['acquisition']={'indices': [['id', 3456], ['id', 9378], ['id', 28468], ['id', 26376], ['id', 38698]], 'labels': [1, 1, 4, 1, 5], 'scores': [0.5589427947998047, 0.5373597741127014, 0.5469917058944702, 0.9573683142662048, 0.8344610333442688]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.0833189487457275})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.55290687084198})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3752667307853699})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31137531995773315})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3480140268802643})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3155680298805237})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.33676469326019287})
store['active_learning_steps'][66]['training']['best_epoch']=4
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9659, 'crossentropy': 0.2875299072265625}
store['active_learning_steps'][66]['acquisition']={'indices': [['id', 17739], ['id', 30900], ['id', 24822], ['id', 56464], ['id', 18417]], 'labels': [5, 5, 4, 9, 5], 'scores': [0.6834427118301392, 0.6426317095756531, 0.4508051872253418, 0.6897343397140503, 0.3041328638792038]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.0190662145614624})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5881257057189941})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.35242024064064026})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3517425060272217})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2998996376991272})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30744996666908264})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3285745680332184})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30523037910461426})
store['active_learning_steps'][67]['training']['best_epoch']=5
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9664, 'crossentropy': 0.2655907958984375}
store['active_learning_steps'][67]['acquisition']={'indices': [['id', 39561], ['id', 39316], ['id', 57270], ['id', 46529], ['id', 9966]], 'labels': [2, 7, 2, 6, 0], 'scores': [0.7174985408782959, 0.5061886608600616, 0.7239741086959839, 0.3687671422958374, 0.7345055341720581]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.119045376777649})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.592323899269104})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3995996415615082})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3873825967311859})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3738488256931305})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.30738040804862976})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31268224120140076})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.33427393436431885})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34723401069641113})
store['active_learning_steps'][68]['training']['best_epoch']=6
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9636, 'crossentropy': 0.2662171875}
store['active_learning_steps'][68]['acquisition']={'indices': [['id', 9559], ['id', 4970], ['id', 7281], ['id', 33198], ['id', 20548]], 'labels': [8, 1, 0, 8, 0], 'scores': [0.6515485048294067, 0.3456267714500427, 0.6518890857696533, 0.5122057199478149, 0.6573435664176941]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0704751014709473})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5119750499725342})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4171621799468994})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3508012294769287})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30120718479156494})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3228233754634857})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2928529977798462})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2915419936180115})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3379688262939453})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3352120518684387})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3302502930164337})
store['active_learning_steps'][69]['training']['best_epoch']=8
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9697, 'crossentropy': 0.24511591796875}
store['active_learning_steps'][69]['acquisition']={'indices': [['id', 37696], ['id', 57728], ['id', 42673], ['id', 15276], ['id', 15832]], 'labels': [2, 9, 1, 7, 9], 'scores': [0.7642833590507507, 0.603151798248291, 0.5920041799545288, 0.7092512249946594, 0.5016525089740753]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.2352700233459473})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.6312718391418457})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.45925694704055786})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4388107657432556})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.37220826745033264})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3558117747306824})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32584065198898315})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3241012990474701})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3501589596271515})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3354067802429199})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3562251925468445})
store['active_learning_steps'][70]['training']['best_epoch']=8
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9693, 'crossentropy': 0.270067529296875}
store['active_learning_steps'][70]['acquisition']={'indices': [['id', 18003], ['id', 5936], ['id', 13318], ['id', 11598], ['id', 42263]], 'labels': [2, 4, 6, 4, 4], 'scores': [0.9322426915168762, 0.7012279033660889, 0.6883261799812317, 0.6383535861968994, 0.5713101327419281]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.196181297302246})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.639764666557312})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3951717019081116})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3672892451286316})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30910152196884155})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3133997321128845})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29067832231521606})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29466888308525085})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28583475947380066})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32496383786201477})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3328326642513275})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30652278661727905})
store['active_learning_steps'][71]['training']['best_epoch']=9
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9716, 'crossentropy': 0.245106787109375}
store['active_learning_steps'][71]['acquisition']={'indices': [['id', 58961], ['id', 27480], ['id', 56654], ['id', 13714], ['id', 32513]], 'labels': [9, 3, 3, 4, 4], 'scores': [0.6598894596099854, 0.7269666194915771, 0.5780479311943054, 0.8388551473617554, 0.6961445808410645]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.241371750831604})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.62725430727005})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4113805890083313})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37909817695617676})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34147781133651733})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3331836462020874})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3466876745223999})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3246878981590271})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30250662565231323})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2996678650379181})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31789690256118774})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3360620141029358})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30717718601226807})
store['active_learning_steps'][72]['training']['best_epoch']=10
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9717, 'crossentropy': 0.2624479248046875}
store['active_learning_steps'][72]['acquisition']={'indices': [['id', 20746], ['id', 15947], ['id', 7270], ['id', 14546], ['id', 52978]], 'labels': [1, 3, 5, 4, 0], 'scores': [0.6899676322937012, 0.7907149195671082, 0.7795301079750061, 0.5837732553482056, 0.6777430772781372]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.1159969568252563})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5468001365661621})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.40932703018188477})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.36122772097587585})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3051687479019165})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29562443494796753})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2777453660964966})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2890382409095764})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2764084041118622})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2854858338832855})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2757791578769684})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30023542046546936})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3291512429714203})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30654335021972656})
store['active_learning_steps'][73]['training']['best_epoch']=11
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9715, 'crossentropy': 0.2382774169921875}
store['active_learning_steps'][73]['acquisition']={'indices': [['id', 4822], ['id', 50583], ['id', 26358], ['id', 42668], ['id', 2779]], 'labels': [4, 4, 3, 9, 9], 'scores': [0.8566712141036987, 0.691283643245697, 0.8470922708511353, 0.6996567845344543, 0.7776539623737335]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.1294854879379272})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5462939143180847})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38984137773513794})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32731205224990845})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29234880208969116})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31248918175697327})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3239246606826782})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25815480947494507})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2836550772190094})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3016994595527649})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2830503284931183})
store['active_learning_steps'][74]['training']['best_epoch']=8
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9729, 'crossentropy': 0.221320947265625}
store['active_learning_steps'][74]['acquisition']={'indices': [['id', 7308], ['id', 56191], ['id', 30865], ['id', 37048], ['id', 50469]], 'labels': [8, 3, 2, 9, 6], 'scores': [0.6571637392044067, 0.6539902687072754, 0.5900046825408936, 0.7749477028846741, 0.693332314491272]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.1486527919769287})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6222870349884033})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4311666488647461})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.35188060998916626})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32119619846343994})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3168306350708008})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28225839138031006})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28570976853370667})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29129403829574585})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30477413535118103})
store['active_learning_steps'][75]['training']['best_epoch']=7
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9681, 'crossentropy': 0.263833056640625}
store['active_learning_steps'][75]['acquisition']={'indices': [['id', 44172], ['id', 56397], ['id', 23766], ['id', 20286], ['id', 8765]], 'labels': [8, 0, 6, 6, 3], 'scores': [0.6394758224487305, 0.6031743288040161, 0.4242343604564667, 0.4763198494911194, 0.6797555685043335]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.2749748229980469})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5928349494934082})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.44892221689224243})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.35466450452804565})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2914595603942871})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29250383377075195})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2836620509624481})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28349432349205017})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30438536405563354})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2998422682285309})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32178038358688354})
store['active_learning_steps'][76]['training']['best_epoch']=8
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9736, 'crossentropy': 0.2314265869140625}
store['active_learning_steps'][76]['acquisition']={'indices': [['id', 34034], ['id', 31347], ['id', 37758], ['id', 49056], ['id', 27916]], 'labels': [8, 3, 0, 7, 8], 'scores': [0.5936349034309387, 0.6923024654388428, 0.7350893020629883, 0.6836373805999756, 0.737571120262146]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.1885335445404053})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5573477745056152})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.44277819991111755})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4106762409210205})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3130223751068115})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35222533345222473})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3217003345489502})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3212236166000366})
store['active_learning_steps'][77]['training']['best_epoch']=5
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9683, 'crossentropy': 0.282396435546875}
store['active_learning_steps'][77]['acquisition']={'indices': [['id', 28844], ['id', 32858], ['id', 48370], ['id', 47936], ['id', 49463]], 'labels': [2, 0, 6, 8, 0], 'scores': [0.6081739664077759, 0.5069226026535034, 0.6192790269851685, 0.6387854814529419, 0.488933801651001]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.1680431365966797})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5756000876426697})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4169093370437622})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4206320345401764})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31276220083236694})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31648728251457214})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29837483167648315})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2942741811275482})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2738834619522095})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27882301807403564})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3234430253505707})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2975495159626007})
store['active_learning_steps'][78]['training']['best_epoch']=9
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9701, 'crossentropy': 0.2457864990234375}
store['active_learning_steps'][78]['acquisition']={'indices': [['id', 21880], ['id', 33162], ['id', 2765], ['id', 39556], ['id', 8265]], 'labels': [2, 8, 0, 5, 6], 'scores': [0.8443187475204468, 0.7737433910369873, 0.8929582238197327, 0.5654349029064178, 0.5919178426265717]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.0897009372711182})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.578964114189148})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3840882182121277})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29676884412765503})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3040822446346283})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2752814292907715})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3315185010433197})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.266954243183136})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2602197527885437})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31746065616607666})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2703639268875122})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27972927689552307})
store['active_learning_steps'][79]['training']['best_epoch']=9
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9724, 'crossentropy': 0.2433486572265625}
store['active_learning_steps'][79]['acquisition']={'indices': [['id', 8714], ['id', 7207], ['id', 29803], ['id', 46126], ['id', 12651]], 'labels': [9, 2, 6, 3, 9], 'scores': [0.899919867515564, 0.8932284712791443, 0.8930436968803406, 0.6951969265937805, 0.6655667424201965]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.205078363418579})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6216701865196228})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.4052072763442993})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34167128801345825})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32253915071487427})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30272576212882996})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28200095891952515})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2922559380531311})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30837130546569824})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25300753116607666})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3106539845466614})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.25385016202926636})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27512168884277344})
store['active_learning_steps'][80]['training']['best_epoch']=10
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.97, 'crossentropy': 0.2484751708984375}
store['active_learning_steps'][80]['acquisition']={'indices': [['id', 391], ['id', 470], ['id', 25661], ['id', 27292], ['ood', 51579]], 'labels': [2, 1, 8, 7, 4], 'scores': [0.6622341871261597, 0.8522266745567322, 0.5125281810760498, 0.79332035779953, 0.47084057331085205]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.235039234161377})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.6204447746276855})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4197511374950409})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3347821831703186})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30218738317489624})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27003830671310425})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27427783608436584})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.25321951508522034})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2847939133644104})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2880983054637909})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26100510358810425})
store['active_learning_steps'][81]['training']['best_epoch']=8
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9691, 'crossentropy': 0.252116943359375}
store['active_learning_steps'][81]['acquisition']={'indices': [['id', 44338], ['id', 25159], ['id', 31301], ['id', 15068], ['id', 6050]], 'labels': [3, 0, 5, 1, 7], 'scores': [0.5569284558296204, 0.8479593992233276, 0.9001849889755249, 0.699146568775177, 0.7561984658241272]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.2472681999206543})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6332331895828247})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.42991864681243896})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3401592969894409})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.34819236397743225})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2830270528793335})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33321481943130493})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28146299719810486})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2812111973762512})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2644616663455963})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26826897263526917})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2613000273704529})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2631019651889801})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2817338705062866})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.25488778948783875})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.28908106684684753})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2561856210231781})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2745020389556885})
store['active_learning_steps'][82]['training']['best_epoch']=15
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9729, 'crossentropy': 0.2348018798828125}
store['active_learning_steps'][82]['acquisition']={'indices': [['id', 15913], ['id', 27632], ['id', 47746], ['id', 49070], ['ood', 9158]], 'labels': [9, 7, 3, 2, 8], 'scores': [0.6754477024078369, 0.7994406819343567, 0.43772730231285095, 0.7316098809242249, 0.3040146827697754]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.1536813974380493})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5689313411712646})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.38907623291015625})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3263894319534302})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29792457818984985})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2812573313713074})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26532554626464844})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2592259645462036})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26305556297302246})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.249246746301651})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2758181393146515})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2752571105957031})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27815449237823486})
store['active_learning_steps'][83]['training']['best_epoch']=10
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9739, 'crossentropy': 0.2224173095703125}
store['active_learning_steps'][83]['acquisition']={'indices': [['id', 5000], ['id', 50916], ['id', 5065], ['id', 39424], ['id', 31677]], 'labels': [7, 4, 2, 5, 0], 'scores': [0.558607429265976, 0.6858632266521454, 0.6744978427886963, 0.5038456618785858, 0.6867522299289703]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.0724595785140991})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5439913868904114})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4055789113044739})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3506566286087036})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3288824260234833})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2740738093852997})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.28606536984443665})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2533155679702759})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.25569984316825867})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2925651967525482})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27713340520858765})
store['active_learning_steps'][84]['training']['best_epoch']=8
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9709, 'crossentropy': 0.2447091064453125}
store['active_learning_steps'][84]['acquisition']={'indices': [['id', 54858], ['id', 9294], ['id', 40891], ['id', 45428], ['id', 37469]], 'labels': [3, 3, 7, 7, 2], 'scores': [0.6732518076896667, 0.7428561449050903, 0.6881928443908691, 0.7322071194648743, 0.858589231967926]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.265136480331421})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.625328540802002})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4429933726787567})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33696988224983215})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3031226396560669})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2864916920661926})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2752085328102112})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3100200295448303})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2704561948776245})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2646205723285675})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2555382251739502})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2691159248352051})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2561214864253998})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2639639377593994})
store['active_learning_steps'][85]['training']['best_epoch']=11
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9712, 'crossentropy': 0.2416724609375}
store['active_learning_steps'][85]['acquisition']={'indices': [['id', 33062], ['id', 18525], ['id', 54981], ['ood', 34516], ['id', 8865]], 'labels': [7, 6, 2, 5, 3], 'scores': [0.8278243541717529, 0.7597079873085022, 0.8331239223480225, 0.6293702125549316, 0.7685665488243103]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.158898115158081})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.6590429544448853})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4578726291656494})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.38170284032821655})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31547558307647705})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2889125347137451})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3067847192287445})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.294114351272583})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29428398609161377})
store['active_learning_steps'][86]['training']['best_epoch']=6
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9664, 'crossentropy': 0.2733798583984375}
