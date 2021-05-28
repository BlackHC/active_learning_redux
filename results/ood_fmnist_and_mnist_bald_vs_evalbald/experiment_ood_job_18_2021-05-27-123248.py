store = {}
store['timestamp']=1622115168
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=18']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=18
store['worker_id']=18
store['num_workers']=80
store['config']={'seed': 1253, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 3792, 5573, 45567, 10508, 2728, 21423, 396, 49512, 31444]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.8473807573318481})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.1904821395874023})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.450857639312744})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.259488105773926})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.4438464641571045})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.6662120819091797})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.473123550415039})
store['active_learning_steps'][0]['training']['best_epoch']=4
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.7063, 'crossentropy': 2.1737583984375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.4636155366897583})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.3979547023773193})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.364556074142456})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.3969652652740479})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.4208719730377197})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.3715856075286865})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 28838], ['id', 31558], ['id', 30782], ['ood', 15938], ['id', 35043]], 'labels': [9, 7, 9, -1, 3], 'scores': [1.0549814495176912, 1.7188471219458115, 2.251231015960925, 2.62352213031195, 2.860436050457193]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.405012607574463})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.500535249710083})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.7673768997192383})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.8815605640411377})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.2646055221557617})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.3820624351501465})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.2079756259918213})
store['active_learning_steps'][1]['training']['best_epoch']=4
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6591, 'crossentropy': 2.6748544921875}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.7207415103912354})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.677748441696167})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.6418089866638184})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.6040310859680176})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.5834102630615234})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.644629716873169})
store['active_learning_steps'][1]['eval_training']['best_epoch']=5
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 38256], ['id', 10811], ['id', 34708], ['id', 48143], ['id', 57296]], 'labels': [2, 5, 0, 5, 0], 'scores': [0.9390372687551263, 1.711040286842909, 2.2519613271013874, 2.6055660044560938, 2.8139808389151746]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.4366495609283447})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.801708698272705})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.2303848266601562})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.3685975074768066})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.3858118057250977})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.1745476722717285})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.0063533782958984})
store['active_learning_steps'][2]['training']['best_epoch']=4
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6777, 'crossentropy': 2.70576484375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.579078197479248})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.6697677373886108})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.630587100982666})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.5331904888153076})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.6174392700195312})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.5427043437957764})
store['active_learning_steps'][2]['eval_training']['best_epoch']=5
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 56848], ['id', 4510], ['id', 57985], ['id', 53570], ['id', 16465]], 'labels': [2, 3, 4, 3, 8], 'scores': [0.9741363915589563, 1.792686909008769, 2.335048446981606, 2.7186235036417186, 2.9451840258278263]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.8531748056411743})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.128200054168701})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.3866219520568848})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.279911518096924})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.515988826751709})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.4101715087890625})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.6348769664764404})
store['active_learning_steps'][3]['training']['best_epoch']=4
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7545, 'crossentropy': 1.9484953125}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.699485182762146})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.599311351776123})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.5637747049331665})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.5411262512207031})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.569908857345581})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.6214300394058228})
store['active_learning_steps'][3]['eval_training']['best_epoch']=4
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 10515], ['id', 49732], ['id', 56531], ['id', 38049], ['id', 40942]], 'labels': [8, 3, 7, 3, 8], 'scores': [0.8145741181338229, 1.5520055187580901, 2.0794705901062853, 2.4337647887203517, 2.677945001624229]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.4778118133544922})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.6113841533660889})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 2.0184273719787598})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.9045326709747314})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.233189105987549})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.78, 'crossentropy': 1.4118330078125}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.281409740447998})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.2275168895721436})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.2040488719940186})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.1010608673095703})
store['active_learning_steps'][4]['eval_training']['best_epoch']=4
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 42383], ['id', 57199], ['id', 47671], ['id', 37310], ['id', 35538]], 'labels': [8, 3, 9, 6, 1], 'scores': [0.6953668265118866, 1.3195591622335878, 1.8086893974799345, 2.13546126264902, 2.3787443461999054]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.7737922668457031})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.2018585205078125})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.2228236198425293})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.3210694789886475})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.4296090602874756})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.3885703086853027})
store['active_learning_steps'][5]['training']['best_epoch']=3
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7276, 'crossentropy': 1.98239140625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.477007269859314})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.361821174621582})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.3462586402893066})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.2343065738677979})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.3513438701629639})
store['active_learning_steps'][5]['eval_training']['best_epoch']=4
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 54461], ['id', 28136], ['id', 45405], ['id', 20059], ['ood', 39182]], 'labels': [5, 8, 2, 4, -1], 'scores': [0.7219362141827392, 1.3586722051199493, 1.812816819408583, 2.1043106220165075, 2.2951310238988123]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.3289580345153809})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.6789488792419434})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.7232871055603027})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 2.074174642562866})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7829, 'crossentropy': 1.1544263671875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.2031691074371338})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.0926626920700073})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.0592114925384521})
store['active_learning_steps'][6]['eval_training']['best_epoch']=1
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 16909], ['id', 37574], ['id', 22641], ['id', 23317], ['id', 22517]], 'labels': [2, 5, 2, 6, 5], 'scores': [0.6218003736094939, 1.1058589058698214, 1.4760063569108688, 1.7404901161059874, 1.9136065178008446]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.1079163551330566})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.3235853910446167})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.3839170932769775})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.539229393005371})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8151, 'crossentropy': 0.9482271484375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.0279209613800049})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 0.9212732911109924})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.8740254044532776})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 21532], ['id', 19942], ['id', 2648], ['id', 17486], ['id', 20500]], 'labels': [5, 5, 2, 7, 3], 'scores': [0.6414242711302443, 1.1826905772415848, 1.6258451145425497, 1.9408112928857122, 2.161972664357993]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.3088037967681885})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.4894819259643555})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.6073434352874756})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.6307990550994873})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.6117174625396729})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.547339677810669})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.8525257110595703})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.8542550802230835})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 2.261012315750122})
store['active_learning_steps'][8]['training']['best_epoch']=6
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7941, 'crossentropy': 1.4436115234375}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.2100481986999512})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.0778753757476807})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.1251938343048096})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.1208982467651367})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.1406049728393555})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.0410914421081543})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.0614142417907715})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.076586127281189})
store['active_learning_steps'][8]['eval_training']['best_epoch']=6
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 5045], ['id', 56713], ['id', 9528], ['id', 5029], ['id', 34154]], 'labels': [9, 9, 8, 8, 8], 'scores': [0.8592524322655335, 1.5949315201156864, 2.13095173927221, 2.4756366550956663, 2.677043090998249]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.1841356754302979})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.4509806632995605})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.4212636947631836})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.7585632801055908})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.6258234977722168})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.4863089323043823})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.7356525659561157})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.5772855281829834})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.7372071743011475})
store['active_learning_steps'][9]['training']['best_epoch']=6
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8299, 'crossentropy': 1.2350177734375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.9941409230232239})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.0314927101135254})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.964511513710022})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9843397736549377})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.8776663541793823})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.93186354637146})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.8887375593185425})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8836026787757874})
store['active_learning_steps'][9]['eval_training']['best_epoch']=8
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 21686], ['id', 5909], ['id', 4904], ['id', 16022], ['id', 28859]], 'labels': [9, 2, 7, 8, 2], 'scores': [0.8181518193284157, 1.5185298213904457, 2.0627505116137432, 2.416312295725052, 2.6547004318131586]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.2858556509017944})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.159243106842041})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.59493088722229})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.486311912536621})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.6281789541244507})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8172, 'crossentropy': 1.03510869140625}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.2093193531036377})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.0364181995391846})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.932160496711731})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 0.9844677448272705})
store['active_learning_steps'][10]['eval_training']['best_epoch']=3
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 7851], ['id', 52516], ['id', 52358], ['id', 27113], ['ood', 14222]], 'labels': [8, 6, 2, 2, -1], 'scores': [0.6538172964361517, 1.2541030950247638, 1.7060903928414568, 2.03674740306141, 2.241383666463811]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.1168413162231445})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.1592345237731934})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.1955749988555908})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.4395108222961426})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.3359320163726807})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.4664057493209839})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.55975341796875})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.7345318794250488})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8446, 'crossentropy': 1.171854296875}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.0816075801849365})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.9730310440063477})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9692797660827637})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.910355806350708})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9388924837112427})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.9342405796051025})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.8837727308273315})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 59543], ['ood', 2591], ['id', 12650], ['id', 13410], ['ood', 53873]], 'labels': [4, -1, 5, 7, -1], 'scores': [0.722888759579752, 1.325632085613822, 1.8195761356473632, 2.1893460938987808, 2.4110446164644186]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9671157598495483})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9975898265838623})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0576802492141724})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.1668341159820557})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0919976234436035})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.2074542045593262})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8757, 'crossentropy': 0.88885244140625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.0034513473510742})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8822358846664429})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8096116185188293})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8519420623779297})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.8472063541412354})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 53358], ['id', 12768], ['id', 30451], ['id', 34906], ['id', 11841]], 'labels': [3, 9, 8, 3, 2], 'scores': [0.7004309714197858, 1.309889460817526, 1.7976654253629016, 2.1408214917108506, 2.3843211207350876]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.1006613969802856})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.2082734107971191})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.3210206031799316})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.3033915758132935})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.2574622631072998})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.2228283882141113})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.3362535238265991})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.4766643047332764})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.5033055543899536})
store['active_learning_steps'][13]['training']['best_epoch']=6
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8582, 'crossentropy': 1.1861658203125}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.1215243339538574})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9694559574127197})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9307818412780762})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8570089936256409})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9134441614151001})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.844813346862793})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8580046892166138})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8268767595291138})
store['active_learning_steps'][13]['eval_training']['best_epoch']=6
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 34713], ['id', 5684], ['id', 39384], ['id', 40517], ['id', 5537]], 'labels': [3, 6, 3, 3, 8], 'scores': [0.7525734133454302, 1.371495126717107, 1.904475253316662, 2.284205181620314, 2.5813121633533402]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.0059459209442139})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.1481518745422363})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.2628926038742065})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.2381479740142822})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.2908886671066284})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.4015507698059082})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8375, 'crossentropy': 1.1086376953125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.096560001373291})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8493853807449341})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7928112745285034})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8154061436653137})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8110892176628113})
store['active_learning_steps'][14]['eval_training']['best_epoch']=3
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 37383], ['id', 1363], ['id', 9442], ['id', 181], ['id', 41713]], 'labels': [3, 0, 4, 3, 0], 'scores': [0.7286380693898227, 1.2834145344288723, 1.7080218106583387, 2.0327530448600957, 2.21876455907125]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9915421009063721})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.0224477052688599})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.2541866302490234})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.401484489440918})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.1965346336364746})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.3187862634658813})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.3647210597991943})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.209169864654541})
store['active_learning_steps'][15]['training']['best_epoch']=5
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8644, 'crossentropy': 1.0225359375}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.045251488685608})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8479599356651306})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7201721668243408})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7468407154083252})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.667102575302124})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.645789623260498})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6899356245994568})
store['active_learning_steps'][15]['eval_training']['best_epoch']=6
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 23190], ['id', 59286], ['id', 30932], ['id', 23982], ['id', 6424]], 'labels': [8, 8, 0, 2, 4], 'scores': [0.8187843064484108, 1.5465210741681283, 2.038417791881538, 2.3784910885577277, 2.623815479196744]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.1124589443206787})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0555078983306885})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9966528415679932})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.2528502941131592})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.3620012998580933})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.0760775804519653})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.4040359258651733})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1816394329071045})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0773882865905762})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.3534619808197021})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.4448390007019043})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.1697635650634766})
store['active_learning_steps'][16]['training']['best_epoch']=9
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8682, 'crossentropy': 1.02315888671875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9391285181045532})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7746033668518066})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7502470016479492})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7137914896011353})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7341235280036926})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7139928340911865})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.698800265789032})
store['active_learning_steps'][16]['eval_training']['best_epoch']=4
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 5194], ['id', 11924], ['id', 50698], ['id', 18106], ['id', 48802]], 'labels': [0, 9, 9, 9, 9], 'scores': [0.7155003739441739, 1.3330595025213303, 1.8515481001709593, 2.2096568387204067, 2.4349158017587484]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9633774161338806})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9277404546737671})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.065878987312317})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.014746904373169})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0776395797729492})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0640738010406494})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1478748321533203})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.1773920059204102})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.266039252281189})
store['active_learning_steps'][17]['training']['best_epoch']=6
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8681, 'crossentropy': 0.9585763671875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.1095173358917236})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8930267095565796})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8144677877426147})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8267525434494019})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7758368253707886})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7713481187820435})
store['active_learning_steps'][17]['eval_training']['best_epoch']=3
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 46232], ['id', 48349], ['id', 47399], ['id', 32894], ['id', 53129]], 'labels': [4, 2, 7, 6, 7], 'scores': [0.7540176791547468, 1.3193633732664454, 1.7663135947129054, 2.1091404754331515, 2.34113581301367]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9669288396835327})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9244284629821777})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9917804002761841})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.08286452293396})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.1192669868469238})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9560601711273193})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.0816680192947388})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.1149111986160278})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.1470179557800293})
store['active_learning_steps'][18]['training']['best_epoch']=6
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8807, 'crossentropy': 0.89397587890625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.0160691738128662})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7988079786300659})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7685285806655884})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7784956693649292})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7453110218048096})
store['active_learning_steps'][18]['eval_training']['best_epoch']=2
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 12934], ['id', 54981], ['id', 25546], ['id', 44346], ['ood', 5612]], 'labels': [8, 2, 8, 6, -1], 'scores': [0.7720704396349449, 1.4204111776806982, 1.9210886177218534, 2.1977385415661184, 2.347053859873153]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9511463642120361})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9507013559341431})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.1477900743484497})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.2545024156570435})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.1904873847961426})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.211491584777832})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.2381560802459717})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.1475188732147217})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8686, 'crossentropy': 1.046423046875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0111275911331177})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8059359788894653})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7929835319519043})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7550960779190063})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7326579093933105})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7328810691833496})
store['active_learning_steps'][19]['eval_training']['best_epoch']=3
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 32454], ['ood', 12005], ['ood', 48192], ['ood', 57827], ['ood', 10765]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.7607269790934086, 1.3159736658127192, 1.7865657882333377, 2.124514278468763, 2.33619475190182]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.152240514755249})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.0670435428619385})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.026598334312439})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.2033231258392334})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.2918004989624023})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.0724869966506958})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.0979712009429932})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.2811667919158936})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.3583588600158691})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.2588844299316406})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.417220115661621})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.2532202005386353})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.33999764919281})
store['active_learning_steps'][20]['training']['best_epoch']=10
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8646, 'crossentropy': 1.22215771484375}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.9789074659347534})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8473961353302002})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7940341234207153})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7979749441146851})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7323060035705566})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7182604074478149})
store['active_learning_steps'][20]['eval_training']['best_epoch']=3
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 33055], ['id', 54278], ['id', 35694], ['id', 59913], ['id', 43950]], 'labels': [6, 7, 9, 2, 9], 'scores': [0.7618245080190327, 1.44689725516251, 2.000653385428394, 2.3687279170348425, 2.5715391180231943]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.0971903800964355})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9478718042373657})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.0577476024627686})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.2175922393798828})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.2185118198394775})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.2074496746063232})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1543431282043457})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.2913237810134888})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.3182564973831177})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8633, 'crossentropy': 1.1321255859375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.0048120021820068})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7702016830444336})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7756052613258362})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.6882606744766235})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.693351149559021})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6383615732192993})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7107124328613281})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.6945123672485352})
store['active_learning_steps'][21]['eval_training']['best_epoch']=6
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 44350], ['id', 35018], ['id', 24022], ['id', 21363], ['id', 25945]], 'labels': [3, 8, 7, 4, 1], 'scores': [0.6873968760782023, 1.293822100541922, 1.8033078056720866, 2.1578187425737037, 2.3958720882192424]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9712842702865601})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8180207014083862})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8573700189590454})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8891326785087585})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9755065441131592})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9970917105674744})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8788, 'crossentropy': 0.797790625}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.0251915454864502})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7053239941596985})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6437382698059082})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.644061803817749})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6375701427459717})
store['active_learning_steps'][22]['eval_training']['best_epoch']=3
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 21990], ['id', 51314], ['id', 50802], ['id', 34368], ['id', 46683]], 'labels': [1, 0, 2, 3, 0], 'scores': [0.7042212726360373, 1.2972202138002027, 1.7480732687136307, 2.0404970891856946, 2.208593110338704]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.0248527526855469})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8335776925086975})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8937853574752808})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8097377419471741})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8382284641265869})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9177169799804688})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8759074211120605})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9085006713867188})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 1.0073256492614746})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.948876678943634})
store['active_learning_steps'][23]['training']['best_epoch']=7
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8866, 'crossentropy': 0.82293974609375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.0103864669799805})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8140164017677307})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7859785556793213})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6838879585266113})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.656067430973053})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7360183000564575})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6181075572967529})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6745690107345581})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6371332406997681})
store['active_learning_steps'][23]['eval_training']['best_epoch']=7
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 20232], ['id', 55194], ['ood', 56086], ['id', 26852], ['id', 45935]], 'labels': [-1, 3, -1, 8, 6], 'scores': [0.7163852636933816, 1.349207498176706, 1.8709354532378901, 2.237024344422127, 2.4393207831762282]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 0.9999704360961914})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.023472547531128})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0425121784210205})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.200724482536316})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0744835138320923})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0109317302703857})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0430582761764526})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.2410669326782227})
store['active_learning_steps'][24]['training']['best_epoch']=5
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8707, 'crossentropy': 0.973806640625}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.1292595863342285})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8159388303756714})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7669864296913147})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.794532299041748})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7526713609695435})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.7657913565635681})
store['active_learning_steps'][24]['eval_training']['best_epoch']=3
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 23849], ['id', 18831], ['ood', 57620], ['id', 15328], ['id', 9192]], 'labels': [7, 4, -1, 2, 3], 'scores': [0.6833095499566577, 1.2863025000398896, 1.751930195675608, 2.1070332527959823, 2.34839555245187]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.0348767042160034})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7900933027267456})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9298985004425049})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.0097712278366089})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8690509796142578})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.1179786920547485})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.1324841976165771})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.1282172203063965})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.875, 'crossentropy': 0.83503662109375}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9251346588134766})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7242977619171143})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.618849515914917})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6086752414703369})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5605602860450745})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6056579351425171})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.5590988993644714})
store['active_learning_steps'][25]['eval_training']['best_epoch']=5
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 19868], ['id', 54913], ['id', 55925], ['id', 1214], ['id', 56286]], 'labels': [5, 5, 4, 8, 8], 'scores': [0.7420114745979083, 1.3178975071125376, 1.7784180396253055, 2.103291808365027, 2.3047132865789797]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8994101881980896})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8488787412643433})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8642209768295288})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9121055603027344})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9785268306732178})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8715618848800659})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8490147590637207})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9798201322555542})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 1.0536572933197021})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.1299726963043213})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.0992966890335083})
store['active_learning_steps'][26]['training']['best_epoch']=8
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8884, 'crossentropy': 0.88579267578125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.0911567211151123})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7942004203796387})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7431240677833557})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.640788733959198})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6286124587059021})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6436960697174072})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6383501887321472})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5936465263366699})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6177771091461182})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5951952338218689})
store['active_learning_steps'][26]['eval_training']['best_epoch']=8
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 6946], ['id', 14825], ['id', 16888], ['id', 40593], ['id', 6415]], 'labels': [1, 3, 0, 4, 3], 'scores': [0.7227734935003516, 1.3369388061831164, 1.8294756365769507, 2.1769478872088506, 2.4340626063339945]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9328145980834961})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6790246963500977})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7062124013900757})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7551164627075195})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6853814721107483})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7405714392662048})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8926247954368591})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9068, 'crossentropy': 0.64856025390625}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9895499348640442})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6328980922698975})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5700951814651489})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5130947828292847})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.497642457485199})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5247769355773926})
store['active_learning_steps'][27]['eval_training']['best_epoch']=4
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 40066], ['id', 21956], ['id', 26656], ['id', 2250], ['ood', 29287]], 'labels': [4, 5, 0, 5, -1], 'scores': [0.6597295224487596, 1.193205098963308, 1.6470209770615392, 1.968185521786328, 2.1906001480897874]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8913590908050537})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6522246599197388})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6635276079177856})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6322596073150635})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7436645030975342})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7525901794433594})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8165991306304932})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9093, 'crossentropy': 0.60521875}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8359432220458984})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5811821222305298})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5097281336784363})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.47488272190093994})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4425426721572876})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4368695020675659})
store['active_learning_steps'][28]['eval_training']['best_epoch']=5
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 38061], ['id', 54043], ['id', 40622], ['id', 40589], ['id', 29085]], 'labels': [2, 2, 2, 2, 2], 'scores': [0.7845094557339869, 1.4310401095034806, 1.9383572822571233, 2.310937291198503, 2.5374243037143644]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8593347668647766})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7334295511245728})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6819179058074951})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6762367486953735})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6927894353866577})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7101819515228271})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7041120529174805})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6971490383148193})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7271605730056763})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6337704658508301})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.7435833215713501})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.7089567184448242})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7708392143249512})
store['active_learning_steps'][29]['training']['best_epoch']=10
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9207, 'crossentropy': 0.6327814453125}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.9977617859840393})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6522986888885498})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6022143959999084})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5334259271621704})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5265635848045349})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.52228844165802})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.49236029386520386})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5162210464477539})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5147838592529297})
store['active_learning_steps'][29]['eval_training']['best_epoch']=6
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 50231], ['id', 50343], ['id', 9727], ['id', 45143], ['id', 40466]], 'labels': [8, 6, 2, 7, 8], 'scores': [0.7452018632802505, 1.398696584964354, 1.9169843747468036, 2.291701933407981, 2.5629468536077384]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9390773773193359})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6858590245246887})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6240795850753784})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.683073878288269})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6935087442398071})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7218260765075684})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.7007348537445068})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6221652030944824})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8525781035423279})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7742283940315247})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.8267756104469299})
store['active_learning_steps'][30]['training']['best_epoch']=8
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9144, 'crossentropy': 0.667943408203125}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9658207893371582})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6564325094223022})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5784155130386353})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5216985940933228})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4790184795856476})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4770435690879822})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.44003361463546753})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4442005753517151})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4509824514389038})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.43449121713638306})
store['active_learning_steps'][30]['eval_training']['best_epoch']=7
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 15779], ['id', 1477], ['id', 36744], ['id', 3594], ['ood', 31260]], 'labels': [0, 4, 1, 9, -1], 'scores': [0.8883077392207024, 1.580585459429873, 2.08814997158383, 2.427942090930046, 2.6360004001881814]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9375805258750916})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6909759640693665})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.583420991897583})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6655757427215576})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7207611203193665})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5758489370346069})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.702494740486145})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6838159561157227})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6812167763710022})
store['active_learning_steps'][31]['training']['best_epoch']=6
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9189, 'crossentropy': 0.5676775390625}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.029050588607788})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6730458736419678})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5406540632247925})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5060681700706482})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5169909000396729})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5045455694198608})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.45467329025268555})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4706956148147583})
store['active_learning_steps'][31]['eval_training']['best_epoch']=8
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 26477], ['ood', 15119], ['id', 24533], ['id', 52099], ['ood', 23731]], 'labels': [2, -1, 8, 2, -1], 'scores': [0.647292375113077, 1.2287505183130807, 1.703960403902868, 2.023384995083722, 2.2464804079471206]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.073911428451538})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6783750653266907})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6985061168670654})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6634359955787659})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5967703461647034})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7459338307380676})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6441701650619507})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.6005494594573975})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7054188251495361})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.655101478099823})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6809803247451782})
store['active_learning_steps'][32]['training']['best_epoch']=8
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9266, 'crossentropy': 0.554982568359375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.056821584701538})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.662926435470581})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5981278419494629})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5173373222351074})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.49495160579681396})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4865052402019501})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4713054299354553})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4437904953956604})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4725712537765503})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.47726544737815857})
store['active_learning_steps'][32]['eval_training']['best_epoch']=9
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 25986], ['id', 38559], ['id', 13235], ['id', 41897], ['id', 53306]], 'labels': [8, 0, 9, 1, 5], 'scores': [0.764235042868848, 1.4233641630094862, 1.937057175595724, 2.276093895347125, 2.480750269811251]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9222527742385864})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5887256860733032})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5841460227966309})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5550692081451416})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5640542507171631})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6038087010383606})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5154494047164917})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5817486047744751})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5414536595344543})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5893608331680298})
store['active_learning_steps'][33]['training']['best_epoch']=7
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9285, 'crossentropy': 0.51790419921875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.0094579458236694})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6180914044380188})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4700230062007904})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4684910774230957})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4456597566604614})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.42953336238861084})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.42305615544319153})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.40026211738586426})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4335261583328247})
store['active_learning_steps'][33]['eval_training']['best_epoch']=7
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 50403], ['id', 10736], ['id', 38608], ['id', 33224], ['id', 5673]], 'labels': [3, 4, 5, 1, 4], 'scores': [0.6354590982583554, 1.2056378362785418, 1.686175277396286, 2.0249629204845565, 2.2508538369344455]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9598342180252075})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5858831405639648})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5156111121177673})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5561474561691284})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.580015242099762})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5405596494674683})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5714575052261353})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5925735235214233})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5702227354049683})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6540162563323975})
store['active_learning_steps'][34]['training']['best_epoch']=7
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9319, 'crossentropy': 0.53262626953125}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.0210211277008057})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6062166690826416})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4805181622505188})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.496121346950531})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.43123793601989746})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.40825846791267395})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4358958899974823})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.40447354316711426})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4092583656311035})
store['active_learning_steps'][34]['eval_training']['best_epoch']=8
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 44298], ['id', 57880], ['id', 13774], ['id', 22573], ['ood', 41194]], 'labels': [2, 9, 2, 2, -1], 'scores': [0.7231707416395596, 1.3943023046872778, 1.921683968381874, 2.2886905975414287, 2.522056158735122]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.0604987144470215})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6692380905151367})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.527219295501709})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5261803865432739})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5155375003814697})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5576551556587219})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5408998727798462})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6039600968360901})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5842597484588623})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5582653284072876})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.7100833058357239})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5482107400894165})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5711309313774109})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5666903257369995})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.6229547262191772})
store['active_learning_steps'][35]['training']['best_epoch']=12
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9363, 'crossentropy': 0.526550927734375}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.1208418607711792})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6850862503051758})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5831289291381836})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5579307079315186})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5105927586555481})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.48736250400543213})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.463035523891449})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4529917240142822})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.432100772857666})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4730618894100189})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.44642168283462524})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.43574097752571106})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.44747039675712585})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4329156279563904})
store['active_learning_steps'][35]['eval_training']['best_epoch']=12
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 5789], ['id', 13752], ['ood', 14487], ['ood', 52707], ['id', 31665]], 'labels': [-1, 9, -1, -1, 2], 'scores': [0.822296563332545, 1.538310400885143, 2.0631856991481525, 2.4387903400555553, 2.6712538032863353]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.0344882011413574})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6088622212409973})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6058312654495239})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6627005338668823})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6199721693992615})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6202374696731567})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5723755359649658})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6951996088027954})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6443763375282288})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6852155923843384})
store['active_learning_steps'][36]['training']['best_epoch']=7
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9212, 'crossentropy': 0.55377646484375}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0328638553619385})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5969980955123901})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5441728830337524})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4759753346443176})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4442765712738037})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4383655786514282})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4310820698738098})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4053068161010742})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.40852081775665283})
store['active_learning_steps'][36]['eval_training']['best_epoch']=8
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 12305], ['id', 4646], ['id', 35606], ['ood', 33953], ['id', 58170]], 'labels': [9, 2, 2, -1, 0], 'scores': [0.7912734192153452, 1.4186370673849917, 1.919065065806146, 2.2898740706930054, 2.521941624643654]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9648364782333374})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5533992052078247})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5254972577095032})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5234208106994629})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5367536544799805})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6553074717521667})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5717102289199829})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5947385430335999})
store['active_learning_steps'][37]['training']['best_epoch']=5
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9253, 'crossentropy': 0.52248056640625}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.0051558017730713})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6329225301742554})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5437536239624023})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4820060729980469})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4825226962566376})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4920995831489563})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4724671244621277})
store['active_learning_steps'][37]['eval_training']['best_epoch']=4
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 40547], ['ood', 59868], ['ood', 42817], ['id', 54880], ['id', 31485]], 'labels': [8, -1, -1, 5, 7], 'scores': [0.6686321192988862, 1.2638727349567276, 1.7410776948060702, 2.0688017598971706, 2.2610365746858605]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9981809854507446})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6541897058486938})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6260205507278442})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6788456439971924})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6842405200004578})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9027, 'crossentropy': 0.60274443359375}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.0188547372817993})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7292223572731018})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6742423176765442})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6591396331787109})
store['active_learning_steps'][38]['eval_training']['best_epoch']=3
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 4066], ['id', 21304], ['id', 57404], ['id', 32776], ['id', 3382]], 'labels': [1, 4, 8, 4, 9], 'scores': [0.6031341023311194, 1.1207623257068424, 1.5456519425581163, 1.8847914417425686, 2.141841252486177]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.014510154724121})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6900973320007324})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.540344774723053})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.55385422706604})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6182747483253479})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.57595294713974})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6807013750076294})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5582090616226196})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5982003808021545})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6070832014083862})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6531072854995728})
store['active_learning_steps'][39]['training']['best_epoch']=8
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9265, 'crossentropy': 0.545847314453125}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.881333589553833})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5548174381256104})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5152004957199097})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.48463737964630127})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.43514376878738403})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4944304823875427})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.38436850905418396})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4245835244655609})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4047871232032776})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3954041600227356})
store['active_learning_steps'][39]['eval_training']['best_epoch']=7
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 43560], ['id', 5600], ['ood', 2706], ['ood', 16469], ['id', 8794]], 'labels': [5, 6, -1, -1, 3], 'scores': [0.8113437125360965, 1.4740889571571674, 2.010466640634281, 2.3287199838462387, 2.5331539806525543]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9967504739761353})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5983202457427979})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.49870240688323975})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5273888111114502})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5310497879981995})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5368859767913818})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5288139581680298})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6096540689468384})
store['active_learning_steps'][40]['training']['best_epoch']=5
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9355, 'crossentropy': 0.4628791015625}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.083082914352417})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5793856382369995})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5186681747436523})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.49630868434906006})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4492274522781372})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4016166031360626})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.43628937005996704})
store['active_learning_steps'][40]['eval_training']['best_epoch']=5
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 1518], ['id', 28633], ['id', 8704], ['id', 34303], ['ood', 27052]], 'labels': [9, 3, 1, 4, -1], 'scores': [0.7140557850392473, 1.3001669865441046, 1.731076452175662, 2.04399990822556, 2.230713041194262]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.0345141887664795})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6270256042480469})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5755801200866699})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5513118505477905})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.656426727771759})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6364585161209106})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6234356164932251})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6943068504333496})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6039789915084839})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.7277070879936218})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6691474914550781})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5827678442001343})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.69317626953125})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6262857913970947})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6177064180374146})
store['active_learning_steps'][41]['training']['best_epoch']=12
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9325, 'crossentropy': 0.535826025390625}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.101426124572754})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.682715654373169})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6190053224563599})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5037295818328857})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5143582224845886})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.48914653062820435})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5062053203582764})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.44741272926330566})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.487680047750473})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.47261056303977966})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4472169280052185})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.44911521673202515})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.47249019145965576})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.43238383531570435})
store['active_learning_steps'][41]['eval_training']['best_epoch']=11
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 41802], ['id', 50904], ['id', 15948], ['id', 34678], ['id', 27770]], 'labels': [2, 5, 2, 8, 2], 'scores': [0.6962699608259859, 1.3255367583371749, 1.828554333273579, 2.1971027517899313, 2.4593781206265577]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.1226613521575928})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6191434264183044})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4940023720264435})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5110841989517212})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4816576838493347})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5529021620750427})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5144906044006348})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4956922233104706})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5897773504257202})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5593522787094116})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5546925067901611})
store['active_learning_steps'][42]['training']['best_epoch']=8
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9444, 'crossentropy': 0.447942333984375}
