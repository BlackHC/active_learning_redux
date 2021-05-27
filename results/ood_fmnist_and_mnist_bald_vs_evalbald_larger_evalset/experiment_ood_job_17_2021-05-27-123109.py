store = {}
store['timestamp']=1622115069
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=17']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=17
store['worker_id']=17
store['num_workers']=80
store['config']={'seed': 1252, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 14640, 45567, 52801, 53689, 801, 55187, 26479, 50997, 3792]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 2.472931385040283})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.171750545501709})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.116522789001465})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.3821253776550293})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.436508893966675})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.4035284519195557})
store['active_learning_steps'][0]['training']['best_epoch']=3
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6081, 'crossentropy': 3.24521640625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.7749354839324951})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.718120813369751})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.732931137084961})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.643883466720581})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.7349234819412231})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 50752], ['ood', 8583], ['id', 7756], ['ood', 28342], ['ood', 37318]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.0620588294816347, 1.908476629083721, 2.4012929026122403, 2.7429278420965817, 2.9157731660150716]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.0114777088165283})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.0610201358795166})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.393038272857666})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 3.254940986633301})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5814, 'crossentropy': 2.0229265625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.3695323467254639})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.3336504697799683})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.3050334453582764})
store['active_learning_steps'][1]['eval_training']['best_epoch']=1
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 1058], ['id', 25144], ['ood', 13428], ['id', 47545], ['id', 34940]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.4402720991628013, 0.7772279168490197, 1.0832183046572261, 1.3027437138960112, 1.4676357413769647]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 1.8510291576385498})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 2.307793140411377})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.544424533843994})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.922159194946289})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 2.790600299835205})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 2.9445691108703613})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.9740781784057617})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 3.0522565841674805})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.076205253601074})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.0721189975738525})
store['active_learning_steps'][2]['training']['best_epoch']=7
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.5731, 'crossentropy': 3.280050390625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.5938869714736938})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.7673259973526})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.8187098503112793})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.6525788307189941})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.769345760345459})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 50221], ['id', 48964], ['ood', 41348], ['id', 50604], ['id', 23053]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.7522502996718206, 1.3657977843283104, 1.851565526602739, 2.204959438774054, 2.4654978271629986]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.454016923904419})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.564453125, 'crossentropy': 2.0500783920288086})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 2.190725088119507})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 2.646402359008789})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 2.985806465148926})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 2.8178396224975586})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.934485673904419})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 2.8040881156921387})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.9643306732177734})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.0618019104003906})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 3.1245665550231934})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.1523537635803223})
store['active_learning_steps'][3]['training']['best_epoch']=9
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.5877, 'crossentropy': 2.9940060546875}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.5120835304260254})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.497192144393921})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.7688229084014893})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.6058857440948486})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.7579392194747925})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.7071582078933716})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.6676840782165527})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.6865050792694092})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.6560158729553223})
store['active_learning_steps'][3]['eval_training']['best_epoch']=6
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 50938], ['id', 44716], ['id', 70], ['id', 31398], ['id', 42499]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.7892320679173185, 1.4447559635083063, 2.024742728949571, 2.4737999883680812, 2.7709031247296023]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.578125, 'crossentropy': 1.6488192081451416})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 2.225508689880371})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 2.543488025665283})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 2.9098103046417236})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 3.322665214538574})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 3.4154582023620605})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 3.3363595008850098})
store['active_learning_steps'][4]['training']['best_epoch']=4
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5736, 'crossentropy': 3.00324765625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.5095224380493164})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.6444941759109497})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.7123908996582031})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.6785101890563965})
store['active_learning_steps'][4]['eval_training']['best_epoch']=1
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 40241], ['id', 41570], ['id', 22546], ['id', 9619], ['id', 56680]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6716274373332911, 1.2830873477562408, 1.7815879680655229, 2.140914138574038, 2.3495202821943346]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.5318204164505005})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 2.015275478363037})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.3846380710601807})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.7320427894592285})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.6356444358825684})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.870065689086914})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.7932229042053223})
store['active_learning_steps'][5]['training']['best_epoch']=4
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.5985, 'crossentropy': 2.5450783203125}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 1.411945104598999})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.5712890625, 'crossentropy': 1.6168410778045654})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.6799602508544922})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.6509331464767456})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.56640625, 'crossentropy': 1.6616342067718506})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 1.6153700351715088})
store['active_learning_steps'][5]['eval_training']['best_epoch']=6
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 42921], ['ood', 14312], ['id', 23580], ['id', 19722], ['id', 55588]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6191176835004166, 1.1390518757904688, 1.5805703640236808, 1.9667865579043262, 2.211978981937202]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 1.3992602825164795})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.872782826423645})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.220674514770508})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.431387424468994})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.3043954372406006})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.5632433891296387})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.4421956539154053})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.7673568725585938})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.661912441253662})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.5652003288269043})
store['active_learning_steps'][6]['training']['best_epoch']=7
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6252, 'crossentropy': 2.5591267578125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.3696587085723877})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.7312120199203491})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.7652658224105835})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.7255468368530273})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.7708051204681396})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.7160741090774536})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.6476058959960938})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.6767477989196777})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.8420538902282715})
store['active_learning_steps'][6]['eval_training']['best_epoch']=8
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 56639], ['id', 44725], ['id', 53691], ['id', 21185], ['id', 9587]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7806937985143572, 1.4810071784577925, 1.9888354020350505, 2.3009791802963298, 2.5468842881717606]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.378643274307251})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.7237651348114014})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.4316272735595703})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.600863456726074})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.74997615814209})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.627396821975708})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.600999116897583})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.7714366912841797})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.1604390144348145})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.0867795944213867})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.1233222484588623})
store['active_learning_steps'][7]['training']['best_epoch']=8
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6322, 'crossentropy': 3.1050478515625}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.3310720920562744})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.5726464986801147})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.9185173511505127})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.811805248260498})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.9683774709701538})
store['active_learning_steps'][7]['eval_training']['best_epoch']=2
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 16799], ['id', 3301], ['id', 48292], ['id', 19842], ['id', 36287]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.6361563989847066, 1.2319230171950721, 1.7003289012960758, 2.048242868759793, 2.2600634250893155]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.58203125, 'crossentropy': 1.3863859176635742})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.6524834632873535})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.3400497436523438})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.4468443393707275})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.2666664123535156})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.6081929206848145})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.853647232055664})
store['active_learning_steps'][8]['training']['best_epoch']=4
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6219, 'crossentropy': 2.323712890625}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.4657410383224487})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.5799291133880615})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.5709331035614014})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.5985556840896606})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.6830193996429443})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.680947184562683})
store['active_learning_steps'][8]['eval_training']['best_epoch']=3
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 39750], ['id', 48480], ['id', 55098], ['id', 31065], ['id', 30012]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.7224318427078325, 1.3358132875648456, 1.8425212110097071, 2.1465966443474755, 2.3903483754189443]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.4080356359481812})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.8067080974578857})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.3235464096069336})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.335628032684326})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.758065938949585})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6222, 'crossentropy': 1.697676953125}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.2453742027282715})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.3216488361358643})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.1956067085266113})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.253990888595581})
store['active_learning_steps'][9]['eval_training']['best_epoch']=3
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 27800], ['id', 36479], ['id', 6311], ['id', 59731], ['id', 6093]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5078411420376983, 0.9440347789757437, 1.2786439064240218, 1.5604852629498698, 1.7886499650549794]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.4173986911773682})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.8018786907196045})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.1976394653320312})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.4386324882507324})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.5932, 'crossentropy': 1.5158919921875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 1.476574182510376})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.3241629600524902})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.3043780326843262})
store['active_learning_steps'][10]['eval_training']['best_epoch']=3
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 51288], ['ood', 44871], ['ood', 30322], ['ood', 59731], ['ood', 1380]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.4916863872196675, 0.91250729024719, 1.259789760442347, 1.5768575548344153, 1.8414504939727898]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.3429745435714722})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.542930006980896})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.8828352689743042})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.394761800765991})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.705037832260132})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.8214268684387207})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.8672103881835938})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6322, 'crossentropy': 2.3865021484375}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.330224633216858})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.555424451828003})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.687396764755249})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.7309564352035522})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.5982284545898438})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.6898987293243408})
store['active_learning_steps'][11]['eval_training']['best_epoch']=3
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 35384], ['id', 49008], ['id', 56945], ['id', 19491], ['id', 36117]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5855223993852434, 1.075226205459603, 1.4306700520961373, 1.7152154091666185, 1.920913446856833]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.4221810102462769})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.6207174062728882})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.974848747253418})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.3232641220092773})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.158632755279541})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.610732078552246})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6134, 'crossentropy': 2.0950064453125}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.3204340934753418})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.2860429286956787})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.2754534482955933})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2669949531555176})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2970685958862305})
store['active_learning_steps'][12]['eval_training']['best_epoch']=5
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 32065], ['id', 24334], ['id', 987], ['id', 1180], ['id', 45096]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5405205808436442, 1.0335473645616884, 1.452000719878546, 1.774560324982696, 2.0170335859988864]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.556640625, 'crossentropy': 1.363773226737976})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.3485052585601807})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.6870019435882568})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.9960980415344238})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.270477771759033})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.0053892135620117})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6431, 'crossentropy': 1.7062662109375}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.3389456272125244})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.2374413013458252})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.2469096183776855})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2028675079345703})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.211434006690979})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 52590], ['id', 8990], ['ood', 27209], ['id', 19567], ['id', 2731]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5201372780482647, 0.9756402817107399, 1.362857427945328, 1.6644611387936363, 1.8861995757743246]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.560546875, 'crossentropy': 1.4638752937316895})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.558889389038086})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.9910593032836914})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.818532943725586})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.3799140453338623})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.590550661087036})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.8845763206481934})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.615746021270752})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.616893768310547})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.4024157524108887})
store['active_learning_steps'][14]['training']['best_epoch']=7
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6313, 'crossentropy': 3.018600390625}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.5615234375, 'crossentropy': 1.467369794845581})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.3260244131088257})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.4976733922958374})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.6361905336380005})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.5710368156433105})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.5282433032989502})
store['active_learning_steps'][14]['eval_training']['best_epoch']=3
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 48483], ['id', 9232], ['ood', 19451], ['id', 1595], ['id', 20809]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5591760823928269, 1.0529743255308124, 1.4867806391070753, 1.8157517696962095, 2.0569824004422035]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.5390625, 'crossentropy': 1.5072413682937622})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.412304162979126})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.702625036239624})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.118945837020874})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 2.328322410583496})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.538689613342285})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.3494176864624023})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6284, 'crossentropy': 2.10501328125}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.381445288658142})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.440750241279602})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.4517736434936523})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.47794508934021})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.4053747653961182})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.5233323574066162})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 19398], ['id', 30660], ['id', 19589], ['id', 1031], ['ood', 39933]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5425104417867124, 1.0329035826793351, 1.4357854788847328, 1.7876595032905351, 2.0670283554547506]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 1.5013134479522705})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2827577590942383})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.613282561302185})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.725820541381836})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.864527702331543})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.143266201019287})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.9807888269424438})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.4529948234558105})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.4776272773742676})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.208034038543701})
store['active_learning_steps'][16]['training']['best_epoch']=7
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6373, 'crossentropy': 2.13853984375}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.3885232210159302})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.3214592933654785})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.4090979099273682})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.3299529552459717})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.3020505905151367})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.3108093738555908})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.283368468284607})
store['active_learning_steps'][16]['eval_training']['best_epoch']=4
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 46593], ['id', 25420], ['id', 52338], ['id', 27400], ['id', 32979]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5520820577389816, 1.0262281122104424, 1.4324837273377717, 1.7312042165484733, 1.9377833490873089]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.38008451461792})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.3043758869171143})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.5772368907928467})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.596898078918457})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.8825433254241943})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.049887180328369})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.9842301607131958})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6552, 'crossentropy': 1.7573466796875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.3086838722229004})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.3024516105651855})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.3070323467254639})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.2558740377426147})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.2780239582061768})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.2521309852600098})
store['active_learning_steps'][17]['eval_training']['best_epoch']=4
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 13708], ['id', 55157], ['id', 58328], ['id', 17738], ['id', 40168]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.49018331266913306, 0.9156085234822227, 1.2627441586751376, 1.5257338487038359, 1.7247756615022611]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.56640625, 'crossentropy': 1.3597373962402344})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.4077880382537842})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.6160531044006348})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.718350887298584})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.161746025085449})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.2149107456207275})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.3715128898620605})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.073518991470337})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.394035816192627})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.7226052284240723})
store['active_learning_steps'][18]['training']['best_epoch']=7
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6397, 'crossentropy': 2.5217767578125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.3271183967590332})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.2748908996582031})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.367341160774231})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.4553883075714111})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.442501425743103})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.4845328330993652})
store['active_learning_steps'][18]['eval_training']['best_epoch']=3
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 25960], ['id', 42953], ['id', 26174], ['ood', 48898], ['id', 44782]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5541198876434641, 1.0249348129544829, 1.4278852441389605, 1.756671571834147, 2.0173181813221257]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.576171875, 'crossentropy': 1.3831512928009033})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.2414019107818604})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.4474103450775146})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.7747530937194824})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.804643154144287})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.20383882522583})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.014693021774292})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.1361794471740723})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6354, 'crossentropy': 1.764898046875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.3676612377166748})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.2347335815429688})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2168900966644287})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2075951099395752})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.160352110862732})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2091331481933594})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.164046287536621})
store['active_learning_steps'][19]['eval_training']['best_epoch']=4
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 22873], ['id', 12428], ['id', 10252], ['id', 3913], ['id', 2809]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.43828134212866443, 0.8546260397902268, 1.1722261377440608, 1.4351690403044541, 1.633156363545618]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.3666383028030396})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.3704814910888672})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.5853657722473145})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.8240420818328857})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.9341470003128052})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.48445200920105})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.4031543731689453})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.1633658409118652})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.719853401184082})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.329652786254883})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.3619165420532227})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.1070566177368164})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.620363712310791})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.631084680557251})
store['active_learning_steps'][20]['training']['best_epoch']=11
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6507, 'crossentropy': 2.3577271484375}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.3155317306518555})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.3250198364257812})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.319381594657898})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.359703779220581})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.477972388267517})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.4330357313156128})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.6028709411621094})
store['active_learning_steps'][20]['eval_training']['best_epoch']=4
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 44704], ['id', 15534], ['id', 56592], ['id', 43735], ['id', 48647]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5533004543820461, 1.0587474198886349, 1.5083397923631754, 1.8630909738797232, 2.0814416783791163]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.3938924074172974})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.279423713684082})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.471825122833252})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.569076657295227})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.7531986236572266})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.8229960203170776})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.045072078704834})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.2477011680603027})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6374, 'crossentropy': 1.6562234375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.291839838027954})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.1774383783340454})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.184227705001831})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.175243854522705})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.1513621807098389})
store['active_learning_steps'][21]['eval_training']['best_epoch']=2
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 24079], ['id', 45234], ['id', 13388], ['id', 1629], ['id', 41949]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5706090324059312, 1.0970822532281566, 1.5433934798785156, 1.8533132538541697, 2.0986357946095673]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.314467430114746})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.3043314218521118})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.3393583297729492})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.6684634685516357})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.731065034866333})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.8648395538330078})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.2703375816345215})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.218334197998047})
store['active_learning_steps'][22]['training']['best_epoch']=5
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6447, 'crossentropy': 1.743130078125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.343691110610962})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.2183544635772705})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.2368484735488892})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.2438039779663086})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.1713066101074219})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.176705002784729})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.21867036819458})
store['active_learning_steps'][22]['eval_training']['best_epoch']=6
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 17753], ['id', 55367], ['id', 28009], ['id', 3878], ['id', 32243]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.611400791992633, 1.121397210571304, 1.565257797132105, 1.9269643909590597, 2.1845526315745225]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.3746464252471924})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.2838702201843262})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.367254614830017})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.5172491073608398})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.7074074745178223})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.9648972749710083})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.915483832359314})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6586, 'crossentropy': 1.51726650390625}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2836389541625977})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1460424661636353})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.0656342506408691})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.0843043327331543})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1118968725204468})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0460565090179443})
store['active_learning_steps'][23]['eval_training']['best_epoch']=6
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 34450], ['id', 41413], ['id', 47164], ['id', 42587], ['ood', 10350]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5203656092676923, 0.972298575832367, 1.3810570454417528, 1.7239431416497126, 2.0004588161560797]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.5703125, 'crossentropy': 1.4069526195526123})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.1800305843353271})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2905428409576416})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.4288790225982666})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.436182975769043})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.6478886604309082})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.7948797941207886})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.8670270442962646})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.9245693683624268})
store['active_learning_steps'][24]['training']['best_epoch']=6
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6479, 'crossentropy': 1.747265234375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.3634538650512695})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1745879650115967})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.141023874282837})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.1510412693023682})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1775944232940674})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.1340112686157227})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1360119581222534})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1259915828704834})
store['active_learning_steps'][24]['eval_training']['best_epoch']=7
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 5537], ['id', 34042], ['id', 9884], ['id', 35418], ['ood', 52716]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5929755919251274, 1.1063052999663823, 1.5344560833962988, 1.9136769923411876, 2.1895289089187253]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.296809434890747})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.1054596900939941})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.251554250717163})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.408090591430664})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.6102385520935059})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.6535136699676514})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.7071478366851807})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.8127448558807373})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6784, 'crossentropy': 1.58413818359375}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.3100601434707642})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1934757232666016})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.111706018447876})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1099140644073486})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1297227144241333})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0625858306884766})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0899927616119385})
store['active_learning_steps'][25]['eval_training']['best_epoch']=6
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 3618], ['id', 41019], ['id', 20388], ['id', 6389], ['id', 41586]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5199471186839277, 0.9885385009253684, 1.3899302013296877, 1.7164752238316954, 1.9589761291960075]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.311034917831421})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.117706060409546})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.2239832878112793})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.494131088256836})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.4979190826416016})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.552448034286499})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6919, 'crossentropy': 1.2540048828125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.548828125, 'crossentropy': 1.4081618785858154})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1805543899536133})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.1367783546447754})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.046229600906372})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.048697829246521})
store['active_learning_steps'][26]['eval_training']['best_epoch']=5
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 19711], ['id', 15078], ['id', 45972], ['id', 56394], ['id', 2649]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.45781043393905363, 0.8633123715085702, 1.2117701304091657, 1.5238438839942274, 1.778031603823254]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.564453125, 'crossentropy': 1.3869590759277344})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1086747646331787})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1706490516662598})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.248146414756775})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.4373486042022705})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.499098777770996})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.6729509830474854})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.697, 'crossentropy': 1.26051416015625}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.3127390146255493})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.117283821105957})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.076685905456543})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.0721967220306396})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0735671520233154})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.0559717416763306})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 31654], ['id', 56414], ['id', 51151], ['id', 55586], ['id', 59953]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.48317087150845195, 0.9165494768281095, 1.2980189187452105, 1.6312572454136247, 1.9066022904364814]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.3474047183990479})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.072281837463379})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1630889177322388})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.2413488626480103})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.2845627069473267})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.5280773639678955})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.5639598369598389})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.64591383934021})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6921, 'crossentropy': 1.26999912109375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.3529560565948486})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1125938892364502})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0451291799545288})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.001685619354248})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 0.9902134537696838})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 0.9989151358604431})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0021339654922485})
store['active_learning_steps'][28]['eval_training']['best_epoch']=7
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 50871], ['id', 47361], ['id', 53509], ['ood', 10884], ['id', 6977]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.554165814202692, 1.0272273917089438, 1.4434247070154926, 1.7747695258709104, 2.0431147299446826]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.5439453125, 'crossentropy': 1.4461091756820679})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.0986950397491455})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0963103771209717})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1673095226287842})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.2400256395339966})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.3801813125610352})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.6143956184387207})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.4874651432037354})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.670184850692749})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.5693333148956299})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.8177567720413208})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.8957690000534058})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.7542624473571777})
store['active_learning_steps'][29]['training']['best_epoch']=10
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.712, 'crossentropy': 1.614637890625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2911362648010254})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1072540283203125})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0540540218353271})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1022250652313232})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.1507935523986816})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.1034317016601562})
store['active_learning_steps'][29]['eval_training']['best_epoch']=3
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 4618], ['id', 42859], ['id', 8449], ['id', 30128], ['id', 40506]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6885390028813503, 1.3079291476355621, 1.7849999082098869, 2.150823376430025, 2.362271627743384]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.2808594703674316})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.104107141494751})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1348453760147095})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.185847520828247})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.2558181285858154})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.3483362197875977})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.3190919160842896})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.5636181831359863})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.5980944633483887})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.6624720096588135})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.7128124237060547})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.8206191062927246})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.692908525466919})
store['active_learning_steps'][30]['training']['best_epoch']=10
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.7061, 'crossentropy': 1.6652197265625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2610188722610474})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0457007884979248})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.09563410282135})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0912399291992188})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0943212509155273})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0630419254302979})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.0985968112945557})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0094828605651855})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0668388605117798})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0780290365219116})
store['active_learning_steps'][30]['eval_training']['best_epoch']=7
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 27179], ['id', 44654], ['id', 56983], ['id', 4762], ['id', 22521]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6162300418295481, 1.1354807021461242, 1.5516545979229521, 1.8537721140660484, 2.0740054047942644]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.3527772426605225})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0549507141113281})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0294432640075684})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.1714625358581543})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.2893218994140625})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.3080998659133911})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.4188072681427002})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.7024, 'crossentropy': 1.13526796875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2974845170974731})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0530431270599365})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.9767210483551025})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 0.9655576944351196})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 0.9798479676246643})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 0.9494420289993286})
store['active_learning_steps'][31]['eval_training']['best_epoch']=6
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 52509], ['id', 17814], ['id', 58130], ['id', 38438], ['id', 5937]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4927071709867541, 0.8803759320399913, 1.2166313518580125, 1.5189110551964653, 1.7415399682065136]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.3974144458770752})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0694615840911865})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.1253795623779297})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.3761820793151855})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.405372142791748})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.4443840980529785})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.5502784252166748})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.5925260782241821})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.655250072479248})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.7035, 'crossentropy': 1.48037177734375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.5673828125, 'crossentropy': 1.3795291185379028})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.122599482536316})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.060704231262207})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0410997867584229})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0521974563598633})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0539910793304443})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0191922187805176})
store['active_learning_steps'][32]['eval_training']['best_epoch']=4
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 9461], ['id', 5893], ['id', 5111], ['id', 7475], ['id', 56380]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6061965472570923, 1.1347889785169423, 1.5773930875173034, 1.9406521158096464, 2.1872080233559785]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.568359375, 'crossentropy': 1.4068493843078613})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.1835072040557861})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1734063625335693})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.2369965314865112})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.3801870346069336})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.5488595962524414})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.5232443809509277})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.5853908061981201})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.7058, 'crossentropy': 1.4417548828125}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 1.449442982673645})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1497422456741333})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0317946672439575})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0253417491912842})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0277290344238281})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0293833017349243})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 0.9598450660705566})
store['active_learning_steps'][33]['eval_training']['best_epoch']=7
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 34750], ['id', 57976], ['id', 4121], ['id', 57827], ['id', 5496]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.580645146146594, 1.041557227184513, 1.4499817628108342, 1.770610012821134, 2.030079441557344]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.4368137121200562})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.1152284145355225})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0797908306121826})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.147818922996521})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.150578498840332})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.4300689697265625})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.360398530960083})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.531410813331604})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.535973310470581})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.7303249835968018})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.7326501607894897})
store['active_learning_steps'][34]['training']['best_epoch']=8
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.7108, 'crossentropy': 1.469655859375}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.3266487121582031})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0630671977996826})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0029464960098267})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 0.9733675718307495})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 0.9830848574638367})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 0.9835058450698853})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9353961944580078})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 0.9427398443222046})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.940386176109314})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 0.9476674795150757})
store['active_learning_steps'][34]['eval_training']['best_epoch']=8
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 11442], ['id', 47462], ['id', 12300], ['id', 45453], ['id', 49863]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.588499596298171, 1.0918499099822139, 1.523410759596799, 1.8622761346717933, 2.1275059782129393]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.3710448741912842})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.1208479404449463})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1517648696899414})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.1158173084259033})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.1985745429992676})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.2629283666610718})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.302527666091919})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.3567534685134888})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.5157248973846436})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.524969220161438})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.6541543006896973})
store['active_learning_steps'][35]['training']['best_epoch']=8
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.7183, 'crossentropy': 1.40257705078125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.313948631286621})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.0612492561340332})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0042719841003418})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.9275548458099365})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 0.9299881458282471})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 0.981246829032898})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9600127935409546})
store['active_learning_steps'][35]['eval_training']['best_epoch']=4
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 35305], ['id', 34821], ['id', 29799], ['id', 59559], ['id', 23684]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5655362505302473, 1.0779559041394768, 1.5101410301141867, 1.8204525962635252, 2.0573443114884986]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.572265625, 'crossentropy': 1.4107255935668945})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1133253574371338})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0307068824768066})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.1174836158752441})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.1432759761810303})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.3345017433166504})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.3810319900512695})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.4315375089645386})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.7062, 'crossentropy': 1.15041103515625}
