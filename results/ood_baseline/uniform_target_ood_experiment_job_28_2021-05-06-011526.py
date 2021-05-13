store = {}
store['timestamp']=1620260126
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=28']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=28
store['worker_id']=28
store['num_workers']=40
store['config']={'seed': 36, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.269864082336426})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.330420732498169})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.940155506134033})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.8919785022735596})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.694, 'crossentropy': 2.022437890625}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 50531], ['id', 51552], ['id', 4739], ['id', 23346], ['id', 51185]], 'labels': [4, 9, 5, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.5903682708740234})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.6727185249328613})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.0427682399749756})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.260958671569824})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6439, 'crossentropy': 2.2257392578125}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 12112], ['id', 50258], ['ood', 13763], ['ood', 31611], ['id', 47699]], 'labels': [8, 8, 7, 0, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.7399218082427979})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.9256339073181152})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.067232131958008})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.440183401107788})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.672, 'crossentropy': 1.56706669921875}
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 56057], ['id', 14098], ['id', 3166], ['ood', 10277], ['ood', 4123]], 'labels': [3, 1, 2, 4, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.7967758178710938})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.9207948446273804})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.410421371459961})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.3324389457702637})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6203, 'crossentropy': 1.7439328125}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 9621], ['id', 1097], ['id', 46200], ['ood', 52618], ['id', 39646]], 'labels': [3, 3, 8, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.4073584079742432})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.633561372756958})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.6723871231079102})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.7275538444519043})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6653, 'crossentropy': 1.40596376953125}
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 39926], ['id', 27759], ['id', 14142], ['id', 33003], ['id', 26440]], 'labels': [8, 1, 9, 0, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.6630005836486816})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.993915319442749})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.9655107259750366})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.2693710327148438})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6532, 'crossentropy': 1.63691669921875}
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 25765], ['ood', 59170], ['id', 54137], ['id', 11480], ['id', 9585]], 'labels': [5, 7, 8, 3, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.4037299156188965})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.5820705890655518})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.6332792043685913})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.6975703239440918})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6879, 'crossentropy': 1.3147533203125}
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 270], ['id', 4469], ['ood', 24280], ['ood', 37503], ['id', 18380]], 'labels': [7, 2, 7, 8, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.5706437826156616})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.6640018224716187})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.8513455390930176})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.8420535326004028})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6856, 'crossentropy': 1.4143654296875}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 49875], ['id', 37593], ['ood', 8370], ['id', 28493], ['id', 30234]], 'labels': [2, 9, 0, 4, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.1912004947662354})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.1865533590316772})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.2791748046875})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.396688461303711})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.3410892486572266})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7694, 'crossentropy': 1.08237490234375}
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 10390], ['id', 4291], ['id', 31039], ['ood', 30322], ['ood', 11309]], 'labels': [5, 1, 8, 7, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.021179437637329})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.1315838098526})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.1789793968200684})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.193110466003418})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7844, 'crossentropy': 1.00627080078125}
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 51245], ['id', 19122], ['ood', 16636], ['ood', 18614], ['ood', 43717]], 'labels': [3, 1, 5, 9, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.1361346244812012})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.122572422027588})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.0834413766860962})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.302978515625})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.18479323387146})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.242387056350708})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7986, 'crossentropy': 0.988972265625}
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 34472], ['id', 11987], ['ood', 32413], ['id', 42250], ['ood', 19923]], 'labels': [8, 7, 6, 0, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 0.9875587224960327})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9114832878112793})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.8992828726768494})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9636178612709045})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.0106778144836426})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9366410970687866})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8375, 'crossentropy': 0.83434296875}
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 27613], ['id', 32531], ['ood', 35547], ['ood', 13486], ['ood', 32027]], 'labels': [7, 0, 8, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 0.9865164756774902})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8587952852249146})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9989044666290283})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.0108870267868042})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9356592893600464})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8361, 'crossentropy': 0.7647126953125}
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 43012], ['id', 42129], ['ood', 20233], ['id', 3578], ['ood', 51149]], 'labels': [4, 9, 5, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.9396774768829346})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.0145905017852783})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.0165233612060547})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.141904592514038})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8066, 'crossentropy': 0.8816595703125}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 45359], ['id', 32017], ['ood', 7139], ['ood', 403], ['id', 51088]], 'labels': [5, 3, 7, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.0051095485687256})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.0016343593597412})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9773104190826416})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.1156117916107178})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.1309475898742676})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.1264915466308594})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8238, 'crossentropy': 0.87061884765625}
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 35884], ['id', 15556], ['id', 5960], ['id', 53868], ['ood', 6444]], 'labels': [5, 4, 4, 9, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.0633983612060547})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 0.9656670093536377})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.042799711227417})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.0666323900222778})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.0977561473846436})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8074, 'crossentropy': 0.8643845703125}
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 5939], ['id', 22177], ['ood', 35068], ['ood', 39743], ['ood', 51292]], 'labels': [1, 2, 1, 6, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 0.9604642391204834})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.8835864067077637})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9663444757461548})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9807710647583008})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.934411883354187})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8326, 'crossentropy': 0.774110791015625}
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 11120], ['id', 29469], ['ood', 7811], ['id', 47459], ['ood', 16115]], 'labels': [3, 0, 3, 9, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9331587553024292})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.9042617082595825})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.8786520957946777})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9584007263183594})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9600567817687988})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9993308782577515})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8358, 'crossentropy': 0.773057470703125}
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 26147], ['ood', 40239], ['ood', 21255], ['ood', 57662], ['ood', 41014]], 'labels': [8, 1, 4, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.9714123606681824})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9082168340682983})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.0216906070709229})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.1811250448226929})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.0370213985443115})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8127, 'crossentropy': 0.85816728515625}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 31445], ['id', 36262], ['id', 17784], ['id', 52890], ['ood', 2598]], 'labels': [0, 3, 8, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0647908449172974})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.9160398244857788})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.0182812213897705})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9889663457870483})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.988457441329956})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8143, 'crossentropy': 0.84666748046875}
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 19912], ['id', 18189], ['id', 43837], ['ood', 56763], ['ood', 58498]], 'labels': [5, 5, 5, 2, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.999147891998291})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8783924579620361})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9021453857421875})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.0231907367706299})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9553409814834595})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8263, 'crossentropy': 0.8104587890625}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 6530], ['id', 51773], ['ood', 32821], ['id', 20357], ['id', 42649]], 'labels': [1, 8, 0, 0, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9019871354103088})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.870018720626831})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8642645478248596})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.827662467956543})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8462599515914917})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8588355779647827})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0252063274383545})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8484, 'crossentropy': 0.7880373046875}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 32264], ['ood', 55924], ['id', 39391], ['id', 28210], ['ood', 24042]], 'labels': [2, 8, 8, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.8960951566696167})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.7906964421272278})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.830838143825531})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9082834124565125})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8663998246192932})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8403, 'crossentropy': 0.74983115234375}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 12882], ['ood', 11166], ['ood', 26249], ['id', 48845], ['ood', 35558]], 'labels': [3, 3, 2, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.9532662630081177})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8007748126983643})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8049907684326172})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9407579898834229})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0211927890777588})
store['active_learning_steps'][23]['training']['best_epoch']=2
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8371, 'crossentropy': 0.76244873046875}
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 46706], ['ood', 48754], ['ood', 28966], ['id', 18396], ['id', 24145]], 'labels': [4, 5, 7, 8, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.8947254419326782})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.7976059913635254})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8171228170394897})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8587034940719604})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8458928465843201})
store['active_learning_steps'][24]['training']['best_epoch']=2
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8476, 'crossentropy': 0.711352392578125}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 53163], ['ood', 27662], ['id', 29783], ['id', 6983], ['ood', 2865]], 'labels': [4, 7, 7, 5, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.0104376077651978})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.765886127948761})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7731467485427856})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8098951578140259})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8684271574020386})
store['active_learning_steps'][25]['training']['best_epoch']=2
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8566, 'crossentropy': 0.732660986328125}
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 5060], ['id', 29633], ['ood', 11482], ['id', 14143], ['ood', 36525]], 'labels': [3, 7, 7, 5, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8428543210029602})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.757025957107544})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.71832275390625})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7582219839096069})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8321124315261841})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8161066770553589})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8697, 'crossentropy': 0.689249658203125}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 9269], ['ood', 35556], ['ood', 43737], ['ood', 40526], ['ood', 59796]], 'labels': [0, 9, 1, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9422286152839661})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7216723561286926})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8125655651092529})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7628397345542908})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7420798540115356})
store['active_learning_steps'][27]['training']['best_epoch']=2
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8489, 'crossentropy': 0.737858447265625}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 32883], ['ood', 23944], ['ood', 5299], ['ood', 8076], ['id', 112]], 'labels': [3, 3, 4, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.038597583770752})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.7808787226676941})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7546466588973999})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.735984206199646})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8964698910713196})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9649816155433655})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9261969327926636})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8678, 'crossentropy': 0.713326171875}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 39856], ['id', 27808], ['ood', 45729], ['ood', 14989], ['ood', 8406]], 'labels': [0, 7, 3, 9, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.9766495823860168})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8677867650985718})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7688730955123901})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8295438289642334})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.88520348072052})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8987295627593994})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8582, 'crossentropy': 0.735770458984375}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 48839], ['ood', 17224], ['id', 59184], ['ood', 29092], ['id', 25355]], 'labels': [6, 0, 9, 6, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9159332513809204})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8101934194564819})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.886744499206543})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8215318918228149})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8775855302810669})
store['active_learning_steps'][30]['training']['best_epoch']=2
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8403, 'crossentropy': 0.75085888671875}
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 59868], ['id', 47926], ['id', 20288], ['id', 56227], ['ood', 12946]], 'labels': [5, 8, 6, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.9659245014190674})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8638511896133423})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8339806199073792})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8404867649078369})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8144346475601196})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8882139325141907})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9207526445388794})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9345254898071289})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8637, 'crossentropy': 0.795633251953125}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 26494], ['ood', 49579], ['ood', 34402], ['ood', 37368], ['ood', 9162]], 'labels': [4, 2, 8, 5, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8370847105979919})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.707589864730835})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7695585489273071})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7137845158576965})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7771881818771362})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8646, 'crossentropy': 0.674413330078125}
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 56916], ['ood', 7909], ['ood', 2180], ['id', 25374], ['ood', 54044]], 'labels': [4, 6, 0, 6, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8913576602935791})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7595973014831543})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7477144598960876})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7319779396057129})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.807906985282898})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8072037696838379})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8158317804336548})
store['active_learning_steps'][33]['training']['best_epoch']=4
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8734, 'crossentropy': 0.7301951171875}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 39569], ['ood', 59537], ['ood', 3671], ['id', 51163], ['ood', 33219]], 'labels': [9, 7, 2, 8, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 0.9594904184341431})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7161848545074463})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.764225959777832})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7365648746490479})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8014981150627136})
store['active_learning_steps'][34]['training']['best_epoch']=2
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8622, 'crossentropy': 0.69431689453125}
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 34712], ['ood', 39060], ['id', 24328], ['ood', 15410], ['id', 37160]], 'labels': [8, 0, 1, 9, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9332597255706787})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7350389957427979})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7261861562728882})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7694438099861145})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7611963748931885})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7657591700553894})
store['active_learning_steps'][35]['training']['best_epoch']=3
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8706, 'crossentropy': 0.6862791015625}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 45048], ['ood', 14043], ['id', 6733], ['ood', 38913], ['id', 58816]], 'labels': [4, 0, 4, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8315951824188232})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7444408535957336})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7344380617141724})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6996830701828003})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7368800640106201})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8216756582260132})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7642803192138672})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8728, 'crossentropy': 0.678559033203125}
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 657], ['id', 51313], ['ood', 27729], ['ood', 32591], ['id', 41549]], 'labels': [5, 8, 4, 6, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8236970901489258})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7416189908981323})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7108098268508911})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7498327493667603})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8199648857116699})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8342180252075195})
store['active_learning_steps'][37]['training']['best_epoch']=3
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.86, 'crossentropy': 0.722298046875}
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 50186], ['id', 28952], ['id', 46428], ['ood', 47205], ['ood', 30307]], 'labels': [8, 5, 8, 7, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9755668640136719})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.6806401014328003})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7262639999389648})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7017607688903809})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7890902757644653})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8578, 'crossentropy': 0.676464111328125}
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 55220], ['ood', 50165], ['ood', 12966], ['id', 31374], ['ood', 50841]], 'labels': [8, 9, 3, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8702377080917358})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7016019821166992})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6839309334754944})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6731494069099426})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7398306727409363})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8220242857933044})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8183621168136597})
store['active_learning_steps'][39]['training']['best_epoch']=4
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8786, 'crossentropy': 0.6589009765625}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 17584], ['ood', 55769], ['ood', 38408], ['id', 1958], ['id', 4663]], 'labels': [5, 3, 9, 7, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9209634065628052})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7482247352600098})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7468377947807312})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7461795210838318})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7065110206604004})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7204198837280273})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.774551272392273})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8126639127731323})
store['active_learning_steps'][40]['training']['best_epoch']=5
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8809, 'crossentropy': 0.699568798828125}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 51881], ['ood', 53648], ['id', 21691], ['ood', 26118], ['ood', 9001]], 'labels': [8, 9, 2, 7, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8802703619003296})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6601183414459229})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6161751747131348})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6404118537902832})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6857308745384216})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7162977457046509})
store['active_learning_steps'][41]['training']['best_epoch']=3
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8901, 'crossentropy': 0.586796826171875}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 45252], ['id', 22792], ['id', 50513], ['id', 35992], ['ood', 3942]], 'labels': [4, 2, 8, 2, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8711272478103638})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6276571750640869})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5756185054779053})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5839838981628418})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6266141533851624})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6566553115844727})
store['active_learning_steps'][42]['training']['best_epoch']=3
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.907, 'crossentropy': 0.513952880859375}
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 4728], ['id', 51646], ['ood', 45568], ['id', 21814], ['ood', 59544]], 'labels': [8, 5, 0, 4, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8561896681785583})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6422330141067505})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6340597867965698})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7287405729293823})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.779347836971283})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6954476833343506})
store['active_learning_steps'][43]['training']['best_epoch']=3
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8846, 'crossentropy': 0.604637939453125}
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 41601], ['id', 40964], ['ood', 27882], ['ood', 1265], ['ood', 27519]], 'labels': [9, 5, 8, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8765101432800293})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6467713117599487})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6434509754180908})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7037078738212585})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6570754051208496})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7225267887115479})
store['active_learning_steps'][44]['training']['best_epoch']=3
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8961, 'crossentropy': 0.565112255859375}
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 43985], ['ood', 31232], ['ood', 14785], ['id', 34072], ['ood', 57726]], 'labels': [2, 3, 2, 9, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.980323314666748})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6583491563796997})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6529662013053894})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6742641925811768})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6267319917678833})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6342364549636841})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6885554790496826})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7254835367202759})
store['active_learning_steps'][45]['training']['best_epoch']=5
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8933, 'crossentropy': 0.58744189453125}
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 54094], ['ood', 38946], ['ood', 20303], ['id', 45183], ['id', 54516]], 'labels': [1, 2, 9, 9, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9733567237854004})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6690378785133362})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6902514100074768})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6087349653244019})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6693977117538452})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6587289571762085})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.708617091178894})
store['active_learning_steps'][46]['training']['best_epoch']=4
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9034, 'crossentropy': 0.56431181640625}
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 31337], ['id', 32664], ['ood', 20791], ['ood', 55818], ['id', 22908]], 'labels': [9, 3, 8, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8668439388275146})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6476382613182068})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6307801008224487})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6452321410179138})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6369633674621582})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6694647073745728})
store['active_learning_steps'][47]['training']['best_epoch']=3
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8964, 'crossentropy': 0.555864599609375}
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 4145], ['ood', 37958], ['ood', 35088], ['ood', 663], ['id', 22562]], 'labels': [0, 2, 8, 9, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9762229919433594})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6495894193649292})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6918604373931885})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6615785360336304})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6908918619155884})
store['active_learning_steps'][48]['training']['best_epoch']=2
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8694, 'crossentropy': 0.642425830078125}
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 19640], ['id', 28831], ['id', 42030], ['ood', 53201], ['ood', 16942]], 'labels': [1, 1, 7, 2, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8598729372024536})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6241265535354614})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5564027428627014})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5739009976387024})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6211355924606323})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6159106492996216})
store['active_learning_steps'][49]['training']['best_epoch']=3
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8989, 'crossentropy': 0.519527734375}
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 38730], ['id', 51059], ['ood', 2588], ['id', 37716], ['ood', 52909]], 'labels': [6, 0, 9, 1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.802822470664978})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.628734827041626})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6253846883773804})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.65630042552948})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6264266967773438})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6715810298919678})
store['active_learning_steps'][50]['training']['best_epoch']=3
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9051, 'crossentropy': 0.543689990234375}
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 6662], ['ood', 58554], ['id', 55675], ['ood', 48599], ['id', 44028]], 'labels': [3, 1, 4, 4, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9116029739379883})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6431958675384521})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5841678977012634})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5423323512077332})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6070994138717651})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6304774284362793})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6210105419158936})
store['active_learning_steps'][51]['training']['best_epoch']=4
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9058, 'crossentropy': 0.533782373046875}
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 28554], ['id', 58976], ['ood', 31084], ['ood', 46327], ['id', 54860]], 'labels': [9, 5, 5, 4, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8741297125816345})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5961123704910278})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6393635272979736})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6068300008773804})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5873833894729614})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6071181893348694})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6108415126800537})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6385847330093384})
store['active_learning_steps'][52]['training']['best_epoch']=5
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9079, 'crossentropy': 0.539747509765625}
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 44780], ['ood', 30242], ['id', 20940], ['id', 57983], ['ood', 47813]], 'labels': [9, 9, 6, 3, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8678584098815918})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5732817649841309})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5890412330627441})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5939680337905884})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6201542615890503})
store['active_learning_steps'][53]['training']['best_epoch']=2
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9044, 'crossentropy': 0.552350439453125}
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 24761], ['id', 23454], ['id', 23933], ['id', 9314], ['ood', 25349]], 'labels': [1, 0, 4, 8, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8714882135391235})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6483221054077148})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6202067136764526})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6421977877616882})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6545709371566772})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.712383508682251})
store['active_learning_steps'][54]['training']['best_epoch']=3
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8972, 'crossentropy': 0.570110009765625}
store['active_learning_steps'][54]['acquisition']={'indices': [['id', 46378], ['ood', 44274], ['ood', 50042], ['id', 22167], ['ood', 17571]], 'labels': [5, 0, 5, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.9500254392623901})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5774405598640442})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5956388711929321})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5827547311782837})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6504570841789246})
store['active_learning_steps'][55]['training']['best_epoch']=2
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.8976, 'crossentropy': 0.56931669921875}
store['active_learning_steps'][55]['acquisition']={'indices': [['ood', 41220], ['ood', 47356], ['ood', 30346], ['ood', 35323], ['ood', 26190]], 'labels': [7, 0, 9, 3, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9342221021652222})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5953164100646973})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5723287463188171})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.593515157699585})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.596210241317749})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6585115194320679})
store['active_learning_steps'][56]['training']['best_epoch']=3
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9094, 'crossentropy': 0.531492626953125}
store['active_learning_steps'][56]['acquisition']={'indices': [['id', 21135], ['id', 4351], ['id', 41609], ['id', 15793], ['id', 28847]], 'labels': [2, 1, 0, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8411151766777039})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6097946166992188})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5975986123085022})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6082830429077148})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6087306141853333})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.641492486000061})
store['active_learning_steps'][57]['training']['best_epoch']=3
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8985, 'crossentropy': 0.550569873046875}
store['active_learning_steps'][57]['acquisition']={'indices': [['id', 52728], ['id', 56459], ['id', 26487], ['id', 47284], ['ood', 2535]], 'labels': [0, 0, 1, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7650117874145508})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5800930857658386})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5336577892303467})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5115585327148438})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5477439761161804})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5641394853591919})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5786857604980469})
store['active_learning_steps'][58]['training']['best_epoch']=4
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9139, 'crossentropy': 0.480533447265625}
store['active_learning_steps'][58]['acquisition']={'indices': [['id', 39271], ['id', 14026], ['ood', 58220], ['ood', 20128], ['id', 41176]], 'labels': [5, 3, 6, 3, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8272433876991272})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.60709547996521})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6029883027076721})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6005617380142212})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6343727111816406})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.629691481590271})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6822546720504761})
store['active_learning_steps'][59]['training']['best_epoch']=4
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.8961, 'crossentropy': 0.552561376953125}
store['active_learning_steps'][59]['acquisition']={'indices': [['ood', 33880], ['id', 6909], ['ood', 17143], ['id', 54159], ['ood', 33293]], 'labels': [0, 6, 2, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8886606097221375})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6772439479827881})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5688609480857849})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.695268988609314})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7392171621322632})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7221207022666931})
store['active_learning_steps'][60]['training']['best_epoch']=3
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8955, 'crossentropy': 0.561662646484375}
store['active_learning_steps'][60]['acquisition']={'indices': [['id', 10083], ['ood', 656], ['id', 5158], ['id', 55899], ['id', 8019]], 'labels': [0, 4, 5, 2, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.796287477016449})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6024119853973389})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5620468854904175})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5767462253570557})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6076669692993164})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6131559610366821})
store['active_learning_steps'][61]['training']['best_epoch']=3
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9061, 'crossentropy': 0.507695556640625}
store['active_learning_steps'][61]['acquisition']={'indices': [['id', 36183], ['ood', 29], ['id', 31148], ['id', 49042], ['ood', 10244]], 'labels': [0, 4, 2, 1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8135019540786743})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6108098030090332})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5819562673568726})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5773110389709473})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5732898712158203})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5477141737937927})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5562397241592407})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6469930410385132})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5820388793945312})
store['active_learning_steps'][62]['training']['best_epoch']=6
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9199, 'crossentropy': 0.48561904296875}
store['active_learning_steps'][62]['acquisition']={'indices': [['id', 50125], ['id', 8979], ['id', 9529], ['ood', 43239], ['id', 27302]], 'labels': [6, 0, 3, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.790062665939331})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6067190170288086})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5651626586914062})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.548399806022644})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5306788682937622})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5429434776306152})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5640114545822144})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5940192341804504})
store['active_learning_steps'][63]['training']['best_epoch']=5
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9137, 'crossentropy': 0.514376513671875}
store['active_learning_steps'][63]['acquisition']={'indices': [['id', 48850], ['ood', 11905], ['ood', 35548], ['id', 9553], ['id', 46824]], 'labels': [5, 5, 4, 3, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8754264116287231})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6045756340026855})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.576077938079834})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6299817562103271})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5923975706100464})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6166038513183594})
store['active_learning_steps'][64]['training']['best_epoch']=3
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9109, 'crossentropy': 0.51892158203125}
store['active_learning_steps'][64]['acquisition']={'indices': [['id', 456], ['id', 16307], ['ood', 56048], ['id', 42923], ['ood', 17877]], 'labels': [8, 1, 7, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7640064358711243})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5723699927330017})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5284016132354736})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5262081623077393})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5161800384521484})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5365498661994934})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5600966811180115})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5540494322776794})
store['active_learning_steps'][65]['training']['best_epoch']=5
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9197, 'crossentropy': 0.47794453125}
store['active_learning_steps'][65]['acquisition']={'indices': [['id', 31821], ['id', 31838], ['ood', 59906], ['id', 58392], ['id', 7280]], 'labels': [5, 5, 0, 6, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7542529106140137})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5453255772590637})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5326344966888428})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5140893459320068})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5191646814346313})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5327380299568176})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5333030223846436})
store['active_learning_steps'][66]['training']['best_epoch']=4
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.918, 'crossentropy': 0.468214453125}
store['active_learning_steps'][66]['acquisition']={'indices': [['id', 59133], ['id', 53173], ['id', 58380], ['ood', 19372], ['id', 40402]], 'labels': [5, 0, 4, 6, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8074560165405273})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5534299612045288})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5420682430267334})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5392647981643677})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5712950229644775})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6025291681289673})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6344289779663086})
store['active_learning_steps'][67]['training']['best_epoch']=4
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9186, 'crossentropy': 0.50719052734375}
store['active_learning_steps'][67]['acquisition']={'indices': [['ood', 30425], ['id', 32005], ['ood', 32087], ['ood', 41179], ['id', 28647]], 'labels': [1, 1, 6, 4, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8892431259155273})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6811219453811646})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5725938081741333})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5305224657058716})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5920114517211914})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5964601635932922})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6063253879547119})
store['active_learning_steps'][68]['training']['best_epoch']=4
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9147, 'crossentropy': 0.48706025390625}
store['active_learning_steps'][68]['acquisition']={'indices': [['id', 27738], ['ood', 1732], ['ood', 34754], ['id', 34858], ['id', 10349]], 'labels': [4, 6, 8, 5, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8566218018531799})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6131457090377808})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5433183908462524})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5893124938011169})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5364384651184082})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5665690898895264})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6356518864631653})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.575555682182312})
store['active_learning_steps'][69]['training']['best_epoch']=5
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9211, 'crossentropy': 0.4829037109375}
store['active_learning_steps'][69]['acquisition']={'indices': [['id', 41673], ['ood', 25195], ['ood', 40590], ['id', 23645], ['id', 10196]], 'labels': [5, 3, 8, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7664796113967896})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5635697841644287})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5063110589981079})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5233356952667236})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5011813640594482})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5326274633407593})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.47009721398353577})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5653226375579834})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5524590015411377})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5232322216033936})
store['active_learning_steps'][70]['training']['best_epoch']=7
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.921, 'crossentropy': 0.468894091796875}
store['active_learning_steps'][70]['acquisition']={'indices': [['ood', 2021], ['id', 50062], ['id', 30271], ['ood', 48355], ['id', 10177]], 'labels': [6, 1, 7, 1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.892281711101532})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5684158802032471})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5638394951820374})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5151671171188354})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5507422089576721})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5261349678039551})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5688704252243042})
store['active_learning_steps'][71]['training']['best_epoch']=4
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9204, 'crossentropy': 0.477912353515625}
store['active_learning_steps'][71]['acquisition']={'indices': [['ood', 11265], ['id', 11352], ['ood', 645], ['id', 44503], ['ood', 57834]], 'labels': [6, 1, 0, 6, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8675049543380737})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5765984058380127})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5963166952133179})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5523594617843628})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5499320030212402})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5420811176300049})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.571273684501648})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5852934122085571})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.607012152671814})
store['active_learning_steps'][72]['training']['best_epoch']=6
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.922, 'crossentropy': 0.481703271484375}
store['active_learning_steps'][72]['acquisition']={'indices': [['id', 440], ['id', 19227], ['ood', 55084], ['ood', 48835], ['ood', 35157]], 'labels': [0, 1, 2, 2, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8234606981277466})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5786323547363281})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5051562786102295})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5259134769439697})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5197708606719971})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5077080726623535})
store['active_learning_steps'][73]['training']['best_epoch']=3
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.921, 'crossentropy': 0.45981044921875}
store['active_learning_steps'][73]['acquisition']={'indices': [['ood', 10137], ['id', 43880], ['id', 38985], ['ood', 46578], ['ood', 7979]], 'labels': [5, 8, 1, 3, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8385775685310364})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5677905678749084})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5353586673736572})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5550605654716492})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5002684593200684})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5269229412078857})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5091015100479126})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5202824473381042})
store['active_learning_steps'][74]['training']['best_epoch']=5
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.919, 'crossentropy': 0.457951708984375}
store['active_learning_steps'][74]['acquisition']={'indices': [['ood', 57018], ['ood', 14093], ['id', 51020], ['ood', 10040], ['ood', 15289]], 'labels': [3, 1, 9, 9, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7912659645080566})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5603256225585938})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5462939739227295})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.561334490776062})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5464157462120056})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.538116455078125})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5967017412185669})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5847452878952026})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5897802114486694})
store['active_learning_steps'][75]['training']['best_epoch']=6
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9165, 'crossentropy': 0.50143974609375}
store['active_learning_steps'][75]['acquisition']={'indices': [['id', 2896], ['id', 51335], ['ood', 59017], ['id', 32492], ['ood', 52977]], 'labels': [4, 7, 8, 5, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8399822115898132})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5589879751205444})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5114167928695679})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4914196729660034})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5883815288543701})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.544055700302124})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5365177989006042})
store['active_learning_steps'][76]['training']['best_epoch']=4
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.924, 'crossentropy': 0.4573759765625}
store['active_learning_steps'][76]['acquisition']={'indices': [['ood', 2479], ['id', 34665], ['ood', 13589], ['ood', 8503], ['id', 23926]], 'labels': [0, 9, 3, 3, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8793302774429321})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5990762114524841})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5171623229980469})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.49517762660980225})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.534349799156189})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5351178646087646})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6192690134048462})
store['active_learning_steps'][77]['training']['best_epoch']=4
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9183, 'crossentropy': 0.45979814453125}
store['active_learning_steps'][77]['acquisition']={'indices': [['ood', 16834], ['id', 48025], ['ood', 36620], ['id', 3247], ['id', 32009]], 'labels': [2, 0, 3, 0, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7769274115562439})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6033083200454712})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5503404140472412})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5387656688690186})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5335949063301086})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5496243238449097})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5599329471588135})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5568413734436035})
store['active_learning_steps'][78]['training']['best_epoch']=5
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9153, 'crossentropy': 0.49400244140625}
store['active_learning_steps'][78]['acquisition']={'indices': [['id', 48212], ['ood', 38406], ['id', 41764], ['ood', 16801], ['id', 20658]], 'labels': [2, 3, 8, 3, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8300166726112366})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5738139152526855})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.576608419418335})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5345349311828613})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5338412523269653})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5620648860931396})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5943655371665955})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5937536954879761})
store['active_learning_steps'][79]['training']['best_epoch']=5
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9164, 'crossentropy': 0.50472861328125}
store['active_learning_steps'][79]['acquisition']={'indices': [['id', 58567], ['ood', 19759], ['id', 120], ['ood', 56866], ['ood', 42936]], 'labels': [1, 8, 2, 7, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.8995394706726074})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.68053138256073})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6085104942321777})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6327247619628906})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5971754789352417})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5986238718032837})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6153574585914612})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6191517114639282})
store['active_learning_steps'][80]['training']['best_epoch']=5
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9086, 'crossentropy': 0.544928173828125}
store['active_learning_steps'][80]['acquisition']={'indices': [['ood', 16246], ['ood', 11032], ['id', 21974], ['id', 51642], ['id', 28102]], 'labels': [6, 0, 3, 2, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8418493270874023})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5873879194259644})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5406999588012695})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.571617603302002})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5440458059310913})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5721150040626526})
store['active_learning_steps'][81]['training']['best_epoch']=3
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9095, 'crossentropy': 0.5051486328125}
store['active_learning_steps'][81]['acquisition']={'indices': [['ood', 20138], ['ood', 14676], ['id', 57300], ['id', 41479], ['ood', 18880]], 'labels': [0, 3, 3, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8692810535430908})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6411107778549194})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5313029289245605})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5364909172058105})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5158692598342896})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5097676515579224})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.550922155380249})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5091459155082703})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5419445037841797})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5971536040306091})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6043572425842285})
store['active_learning_steps'][82]['training']['best_epoch']=8
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9244, 'crossentropy': 0.4884705078125}
store['active_learning_steps'][82]['acquisition']={'indices': [['ood', 25723], ['id', 45528], ['id', 5934], ['ood', 25420], ['ood', 21503]], 'labels': [6, 9, 5, 9, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8049335479736328})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6284743547439575})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5308331847190857})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5633463859558105})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5762958526611328})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5395413637161255})
store['active_learning_steps'][83]['training']['best_epoch']=3
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9148, 'crossentropy': 0.486356884765625}
store['active_learning_steps'][83]['acquisition']={'indices': [['id', 47386], ['ood', 56402], ['id', 59046], ['ood', 48323], ['ood', 47544]], 'labels': [0, 3, 3, 4, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8415571451187134})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5493679046630859})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5226579904556274})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5583181381225586})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5763006210327148})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6095653772354126})
store['active_learning_steps'][84]['training']['best_epoch']=3
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9127, 'crossentropy': 0.491092431640625}
store['active_learning_steps'][84]['acquisition']={'indices': [['ood', 32743], ['id', 30453], ['ood', 7891], ['ood', 52388], ['id', 55709]], 'labels': [4, 9, 1, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8527567982673645})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.60032719373703})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.535682201385498})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5668891668319702})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5798712968826294})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6155966520309448})
store['active_learning_steps'][85]['training']['best_epoch']=3
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9154, 'crossentropy': 0.46995966796875}
store['active_learning_steps'][85]['acquisition']={'indices': [['id', 44489], ['ood', 7272], ['id', 56633], ['id', 32827], ['id', 45219]], 'labels': [9, 9, 1, 3, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8545517325401306})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6533666849136353})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.53523850440979})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5629387497901917})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5956692099571228})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5971699953079224})
store['active_learning_steps'][86]['training']['best_epoch']=3
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9123, 'crossentropy': 0.48233720703125}
