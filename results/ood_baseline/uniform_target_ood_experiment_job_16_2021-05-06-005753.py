store = {}
store['timestamp']=1620259073
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=16']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=16
store['worker_id']=16
store['num_workers']=40
store['config']={'seed': 20, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 50, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.356658458709717})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.65586519241333})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.6641464233398438})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.126467704772949})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6829, 'crossentropy': 2.0237904296875}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 43248], ['id', 19205], ['id', 42663], ['id', 37823], ['id', 47605]], 'labels': [9, 3, 5, 5, 3], 'scores': [0.6920938491821289, 0.6518774628639221, 0.8273398280143738, 0.8216599225997925, 0.8876224160194397]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.6191482543945312})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.782742500305176})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.9724204540252686})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.137427568435669})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6357, 'crossentropy': 2.342861328125}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 42053], ['ood', 50318], ['id', 51452], ['id', 46330], ['id', 26985]], 'labels': [0, 7, 7, 8, 4], 'scores': [0.6441144943237305, 0.5809230804443359, 0.8908867239952087, 0.919045627117157, 0.8173050284385681]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.6321163177490234})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.971785068511963})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.9624223709106445})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.2593863010406494})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7328, 'crossentropy': 1.41552451171875}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 42920], ['id', 25576], ['id', 44083], ['id', 30873], ['id', 54484]], 'labels': [8, 0, 9, 6, 2], 'scores': [0.6271792054176331, 0.7000547647476196, 0.5467821955680847, 0.5805928707122803, 0.700490415096283]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.4680259227752686})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.6459776163101196})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.7786245346069336})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 2.1157569885253906})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7491, 'crossentropy': 1.39325322265625}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 4315], ['id', 53647], ['id', 48952], ['ood', 57414], ['id', 5062]], 'labels': [9, 5, 7, 5, 9], 'scores': [0.5698524713516235, 0.7034340500831604, 0.7888267636299133, 0.3168386220932007, 0.8471843600273132]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.2796809673309326})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.7981388568878174})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.7936937808990479})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.8748798370361328})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7599, 'crossentropy': 1.1803775390625}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 26742], ['id', 21399], ['id', 5774], ['id', 46890], ['id', 8799]], 'labels': [7, 8, 6, 5, 6], 'scores': [0.6012662649154663, 0.639856219291687, 0.6153268814086914, 0.6173673868179321, 0.7885477542877197]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.3238348960876465})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.655380368232727})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.7996344566345215})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.712306022644043})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.75, 'crossentropy': 1.25757158203125}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 21390], ['id', 45535], ['id', 46746], ['id', 792], ['id', 49784]], 'labels': [3, 7, 0, 8, 5], 'scores': [0.6076784729957581, 0.5239320993423462, 0.5363836288452148, 0.527310848236084, 0.53103107213974]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.1500234603881836})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.5758016109466553})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.6211943626403809})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.547349452972412})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7672, 'crossentropy': 1.1039798828125}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 56152], ['id', 7954], ['id', 13413], ['id', 20013], ['id', 58058]], 'labels': [9, 0, 1, 6, 8], 'scores': [0.6097030639648438, 0.6313588619232178, 0.536700963973999, 0.5397144556045532, 0.6564465761184692]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.197160243988037})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.283973217010498})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.4446841478347778})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.2285099029541016})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7777, 'crossentropy': 1.1377453125}
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 14092], ['id', 31249], ['id', 43588], ['id', 39074], ['id', 12940]], 'labels': [1, 3, 8, 2, 5], 'scores': [0.39620935916900635, 0.6033386588096619, 0.49896538257598877, 0.5488733649253845, 0.5684683322906494]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.0504043102264404})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.2168941497802734})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.3584845066070557})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.4411941766738892})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7764, 'crossentropy': 1.03491962890625}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 32836], ['id', 3268], ['id', 10896], ['id', 32427], ['id', 42701]], 'labels': [2, 6, 3, 0, 1], 'scores': [0.4553673267364502, 0.5646724700927734, 0.5802664756774902, 0.6538389921188354, 0.5189043283462524]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9992554187774658})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.062708854675293})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0929863452911377})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.1437158584594727})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7936, 'crossentropy': 0.9611935546875}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 58429], ['id', 47437], ['id', 25462], ['id', 32351], ['id', 58884]], 'labels': [2, 6, 6, 9, 2], 'scores': [0.678684413433075, 0.525860607624054, 0.7036449909210205, 0.4613989591598511, 0.4328080415725708]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.0287600755691528})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.0789539813995361})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.0899407863616943})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.1308510303497314})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7901, 'crossentropy': 0.95973271484375}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 2859], ['ood', 33391], ['id', 59716], ['id', 25116], ['id', 19316]], 'labels': [4, 0, 4, 3, 6], 'scores': [0.5331944823265076, 0.370922327041626, 0.3373933434486389, 0.44990891218185425, 0.5705347657203674]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.7555820941925049})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7511110901832581})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8873972296714783})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0074185132980347})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9740341901779175})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8606, 'crossentropy': 0.71925146484375}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 37337], ['ood', 10534], ['id', 6144], ['id', 8255], ['id', 14757]], 'labels': [1, 3, 2, 1, 7], 'scores': [0.6470935940742493, 0.2986619472503662, 0.43326789140701294, 0.6451243162155151, 0.40637052059173584]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.7675150632858276})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7742756009101868})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8800519704818726})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8335806727409363})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8509, 'crossentropy': 0.734753173828125}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 27239], ['id', 43152], ['id', 26852], ['ood', 2142], ['id', 32223]], 'labels': [2, 4, 8, 5, 3], 'scores': [0.5382080078125, 0.3962717652320862, 0.437577486038208, 0.4038994312286377, 0.3824678659439087]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7529029846191406})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6801356673240662})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7478222846984863})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7499758005142212})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.830521821975708})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8917, 'crossentropy': 0.615539990234375}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 37770], ['id', 47076], ['id', 46631], ['id', 44882], ['id', 27641]], 'labels': [7, 8, 8, 9, 2], 'scores': [0.46513232588768005, 0.6704864501953125, 0.621592104434967, 0.5835927724838257, 0.821722686290741]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7279094457626343})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6825116276741028})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6665506958961487})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7548497915267944})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7467174530029297})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8021968603134155})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8994, 'crossentropy': 0.594052783203125}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 35065], ['id', 32504], ['id', 14210], ['id', 51987], ['id', 42336]], 'labels': [9, 9, 3, 3, 2], 'scores': [0.36798349022865295, 0.7669690251350403, 0.7135312557220459, 0.7250921726226807, 0.4291631579399109]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.8884643316268921})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6651232242584229})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7190505862236023})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6882162094116211})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7256920337677002})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8934, 'crossentropy': 0.624445263671875}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 38280], ['id', 24740], ['id', 6418], ['id', 59663], ['id', 26034]], 'labels': [5, 8, 5, 8, 5], 'scores': [0.5127456188201904, 0.7753980755805969, 0.6832418441772461, 0.6535866856575012, 0.8649615049362183]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8470835089683533})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6573494076728821})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.657495379447937})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7958676815032959})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7147871255874634})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8907, 'crossentropy': 0.622448681640625}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 54068], ['id', 10244], ['id', 34314], ['id', 48279], ['id', 49192]], 'labels': [6, 5, 7, 2, 2], 'scores': [0.5254949331283569, 0.8567070960998535, 0.6607165932655334, 0.6726125478744507, 0.7341904640197754]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7447917461395264})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6384822726249695})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6510374546051025})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7328068614006042})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6939659118652344})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8875, 'crossentropy': 0.597504736328125}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 11208], ['id', 22784], ['id', 51283], ['id', 50239], ['id', 2184]], 'labels': [9, 8, 5, 9, 2], 'scores': [0.7634081840515137, 0.43273013830184937, 0.670702338218689, 0.7733551859855652, 0.6443836092948914]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7291125059127808})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6093258857727051})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6624634265899658})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7047361135482788})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6326441764831543})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.897, 'crossentropy': 0.593223193359375}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 33357], ['id', 52460], ['id', 48507], ['id', 22579], ['id', 2927]], 'labels': [3, 7, 6, 2, 8], 'scores': [0.7073431611061096, 0.5554894208908081, 0.6719280481338501, 0.7488055229187012, 0.6013129353523254]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8682540059089661})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5703421831130981})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5754015445709229})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6574654579162598})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7271670699119568})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9172, 'crossentropy': 0.52125107421875}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 8924], ['id', 6406], ['id', 23190], ['id', 38092], ['id', 3326]], 'labels': [2, 0, 8, 8, 5], 'scores': [0.8290746808052063, 0.6431741118431091, 0.7914822697639465, 0.553823709487915, 0.5531392693519592]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8209434747695923})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6258549094200134})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5379012823104858})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.632052481174469})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6034494042396545})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6889698505401611})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9158, 'crossentropy': 0.5197357421875}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 49582], ['id', 31844], ['id', 15623], ['id', 52770], ['id', 46623]], 'labels': [2, 7, 8, 9, 4], 'scores': [0.6559520959854126, 0.6242818236351013, 0.7125747203826904, 0.5261242389678955, 0.5580816864967346]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7750067710876465})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.62565016746521})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5365376472473145})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5335502028465271})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5909409523010254})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5934815406799316})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5582034587860107})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9287, 'crossentropy': 0.45533818359375}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 26230], ['id', 9904], ['id', 30088], ['id', 53736], ['id', 37397]], 'labels': [0, 3, 0, 9, 3], 'scores': [0.72788867354393, 0.7290891408920288, 0.7555828094482422, 0.9198307991027832, 0.5759294629096985]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8489977121353149})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5969797372817993})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5163578987121582})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5709412097930908})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6115447282791138})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5746721029281616})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9229, 'crossentropy': 0.518857666015625}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 26079], ['id', 20206], ['id', 19086], ['id', 38316], ['id', 58881]], 'labels': [8, 7, 7, 4, 3], 'scores': [0.74088454246521, 0.7005934119224548, 0.6519646644592285, 0.5963015556335449, 0.7848003506660461]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.0174812078475952})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6688075065612793})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6127930879592896})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5305933356285095})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6033945083618164})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6378653049468994})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.593989372253418})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9228, 'crossentropy': 0.501464892578125}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 16190], ['id', 55896], ['id', 25326], ['id', 53909], ['id', 966]], 'labels': [3, 7, 8, 6, 3], 'scores': [0.9534906148910522, 0.6875682473182678, 0.48246288299560547, 0.7822935879230499, 0.8374431133270264]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8101567029953003})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5189406871795654})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5102810859680176})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5335221290588379})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5293301343917847})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5207109451293945})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9238, 'crossentropy': 0.465822119140625}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 35051], ['id', 10481], ['ood', 22674], ['id', 22593], ['id', 26588]], 'labels': [2, 6, 9, 7, 4], 'scores': [0.8156013488769531, 0.7531002163887024, 0.39396870136260986, 0.4543275833129883, 0.7606189250946045]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8654968738555908})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5933319330215454})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5375881195068359})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5053701400756836})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.543771505355835})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5491592884063721})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5897071361541748})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9318, 'crossentropy': 0.43061201171875}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 34739], ['id', 6269], ['id', 59446], ['id', 37631], ['id', 1239]], 'labels': [9, 3, 5, 2, 8], 'scores': [0.89779132604599, 0.7515065670013428, 0.688484400510788, 0.6333796977996826, 0.6970853209495544]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9167486429214478})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5920478105545044})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5075892210006714})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5583932399749756})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5731186866760254})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5679522156715393})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.923, 'crossentropy': 0.467538330078125}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 52866], ['id', 37402], ['id', 53083], ['id', 45749], ['id', 46329]], 'labels': [7, 7, 3, 4, 3], 'scores': [0.530799150466919, 0.5379289388656616, 0.6460181474685669, 0.5359058380126953, 0.7044516205787659]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8109148740768433})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.49389663338661194})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5141679048538208})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5269346237182617})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5426270365715027})
store['active_learning_steps'][27]['training']['best_epoch']=2
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9288, 'crossentropy': 0.44927529296875}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 44172], ['id', 8833], ['id', 47322], ['id', 2258], ['id', 27282]], 'labels': [8, 2, 8, 5, 3], 'scores': [0.704908013343811, 0.6341394186019897, 0.5292706489562988, 0.7277076244354248, 0.4432902932167053]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.9821314215660095})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5913389921188354})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5181115865707397})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.503732442855835})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5144275426864624})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5421359539031982})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5629379153251648})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9237, 'crossentropy': 0.492754736328125}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 10221], ['id', 45218], ['id', 39320], ['id', 13742], ['id', 58413]], 'labels': [0, 0, 6, 9, 9], 'scores': [0.5800259113311768, 0.6916223764419556, 0.6757164001464844, 0.7693402469158173, 0.6916898190975189]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8512436151504517})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5830023288726807})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5445635318756104})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.47471773624420166})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4851934313774109})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.558566689491272})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5344455242156982})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9297, 'crossentropy': 0.4376787109375}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 53231], ['id', 28506], ['ood', 8663], ['id', 53867], ['id', 46736]], 'labels': [3, 8, 1, 4, 3], 'scores': [0.3856615424156189, 0.774124026298523, 0.330125093460083, 0.5453466773033142, 0.7852736115455627]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8355627059936523})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5631523132324219})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5243377089500427})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5256388783454895})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5801421403884888})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5588470697402954})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9215, 'crossentropy': 0.488814013671875}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 6684], ['id', 19396], ['id', 38184], ['id', 15616], ['id', 19124]], 'labels': [0, 5, 7, 8, 8], 'scores': [0.5663429498672485, 0.6135518550872803, 0.5683673024177551, 0.6201483607292175, 0.7268756628036499]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8968244791030884})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5558031797409058})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5158296823501587})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4850359261035919})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5384634733200073})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6151028871536255})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5837920904159546})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9278, 'crossentropy': 0.4478298828125}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 14074], ['id', 28412], ['ood', 56978], ['id', 34811], ['id', 43636]], 'labels': [5, 0, 4, 5, 4], 'scores': [0.6984525918960571, 0.5543557405471802, 0.41331613063812256, 0.48609459400177, 0.6675796508789062]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9049307107925415})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5362376570701599})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5264992713928223})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.48221278190612793})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.49564701318740845})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.49351680278778076})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5020501017570496})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9331, 'crossentropy': 0.434336083984375}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 18398], ['id', 31756], ['id', 44013], ['id', 51856], ['id', 17153]], 'labels': [4, 5, 4, 7, 2], 'scores': [0.6806447505950928, 0.5568799376487732, 0.7772526741027832, 0.7022835612297058, 0.6476126909255981]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8137985467910767})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5477488040924072})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5479775071144104})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.46935170888900757})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.466208815574646})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4716527462005615})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5361562371253967})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5276987552642822})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9427, 'crossentropy': 0.407187646484375}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 28305], ['id', 28914], ['id', 21454], ['id', 23788], ['id', 42415]], 'labels': [0, 4, 0, 1, 7], 'scores': [0.5968766212463379, 0.5764508843421936, 0.6276857852935791, 0.7257944941520691, 0.8833295702934265]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8829021453857422})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.480400025844574})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4089013636112213})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4315080940723419})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.42229145765304565})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4715427756309509})
store['active_learning_steps'][34]['training']['best_epoch']=3
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9373, 'crossentropy': 0.409140087890625}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 14974], ['id', 11534], ['id', 8780], ['id', 15510], ['id', 35694]], 'labels': [9, 7, 8, 2, 9], 'scores': [0.48368895053863525, 0.6352746486663818, 0.6195129156112671, 0.5126608610153198, 0.621579647064209]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8721804618835449})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5680665969848633})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4711264371871948})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.45219171047210693})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.42085474729537964})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4589793086051941})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.442950963973999})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.45127737522125244})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9427, 'crossentropy': 0.38988662109375}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 4058], ['id', 58623], ['id', 21525], ['id', 36704], ['id', 53873]], 'labels': [8, 6, 3, 2, 4], 'scores': [0.8835259675979614, 0.5610758662223816, 0.8429118990898132, 0.8611432909965515, 0.7736386060714722]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8765702247619629})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5254505276679993})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4963831603527069})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.45607924461364746})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4759643077850342})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4698890745639801})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.46959155797958374})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9426, 'crossentropy': 0.380383056640625}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 935], ['id', 48006], ['id', 26206], ['id', 25055], ['id', 10412]], 'labels': [8, 6, 5, 3, 5], 'scores': [0.5365427732467651, 0.7551402747631073, 0.78010094165802, 0.6230390071868896, 0.5712884068489075]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9155608415603638})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5391435623168945})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.464127779006958})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4866703152656555})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4522044062614441})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.42247331142425537})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.43268823623657227})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.48040157556533813})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.47481027245521545})
store['active_learning_steps'][37]['training']['best_epoch']=6
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.942, 'crossentropy': 0.4062504150390625}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 28920], ['id', 57211], ['id', 34946], ['id', 49889], ['id', 344]], 'labels': [2, 5, 8, 0, 9], 'scores': [0.8845950961112976, 0.7540895938873291, 0.851057767868042, 0.7747130990028381, 0.6826167106628418]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.00697660446167})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5952733755111694})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4634774327278137})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.46724289655685425})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.42905694246292114})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.47910410165786743})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4343360662460327})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.48948463797569275})
store['active_learning_steps'][38]['training']['best_epoch']=5
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9474, 'crossentropy': 0.3785616943359375}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 15771], ['id', 52686], ['id', 51207], ['id', 12089], ['id', 21838]], 'labels': [5, 5, 8, 3, 6], 'scores': [0.5791761875152588, 0.6852472722530365, 0.8062095642089844, 0.7590409517288208, 0.49967214465141296]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9124536514282227})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5831015110015869})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.45377469062805176})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4415431022644043})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3889014422893524})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3992060422897339})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41260892152786255})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.44456565380096436})
store['active_learning_steps'][39]['training']['best_epoch']=5
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9441, 'crossentropy': 0.3875032470703125}
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 25868], ['id', 10044], ['id', 12614], ['id', 9627], ['id', 9631]], 'labels': [5, 6, 9, 2, 9], 'scores': [0.39359283447265625, 0.7587414383888245, 0.5843743681907654, 0.5046899318695068, 0.5661214590072632]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.0312061309814453})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5471267700195312})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.45348870754241943})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4399572014808655})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.40278521180152893})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4298863410949707})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3938593864440918})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4266609251499176})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.426194965839386})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.40150195360183716})
store['active_learning_steps'][40]['training']['best_epoch']=7
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.947, 'crossentropy': 0.3852820068359375}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 54377], ['id', 59339], ['id', 720], ['id', 41299], ['id', 17712]], 'labels': [3, 1, 8, 3, 3], 'scores': [0.7282212376594543, 0.9712544679641724, 0.701258659362793, 0.7998889088630676, 0.9262397289276123]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9577862024307251})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5633770227432251})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4492173194885254})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4486497640609741})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39142102003097534})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3706076741218567})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3917420208454132})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3398582339286804})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.413237601518631})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3686012923717499})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4366025924682617})
store['active_learning_steps'][41]['training']['best_epoch']=8
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9576, 'crossentropy': 0.3393095458984375}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 28374], ['id', 23582], ['id', 54954], ['id', 10918], ['id', 27795]], 'labels': [3, 8, 8, 4, 3], 'scores': [0.7555770874023438, 0.4222947955131531, 0.783997118473053, 0.804044097661972, 0.8288776874542236]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9195057153701782})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5162851214408875})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4551013708114624})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.39837968349456787})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3748167157173157})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3486395478248596})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36115962266921997})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3913510739803314})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3627690076828003})
store['active_learning_steps'][42]['training']['best_epoch']=6
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9546, 'crossentropy': 0.3310349365234375}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 54190], ['id', 51255], ['id', 47506], ['id', 49064], ['id', 19450]], 'labels': [8, 4, 8, 8, 2], 'scores': [0.47451531887054443, 0.6402403712272644, 0.8667751550674438, 0.8355474472045898, 0.7154396772384644]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9429274797439575})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.46927565336227417})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3773677349090576})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3853357136249542})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4054087698459625})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.36592161655426025})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.38417738676071167})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4005959630012512})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.41991183161735535})
store['active_learning_steps'][43]['training']['best_epoch']=6
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.952, 'crossentropy': 0.3349528564453125}
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 10195], ['id', 41349], ['id', 24193], ['id', 17365], ['id', 50881]], 'labels': [0, 9, 9, 0, 5], 'scores': [0.70733642578125, 0.43908464908599854, 0.7415991425514221, 0.5920403599739075, 0.6467734575271606]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.0790671110153198})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.516168475151062})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4267878234386444})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.39642298221588135})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.34746307134628296})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.38836294412612915})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34566545486450195})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3741818070411682})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.40466517210006714})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.41420286893844604})
store['active_learning_steps'][44]['training']['best_epoch']=7
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9556, 'crossentropy': 0.3189870361328125}
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 51848], ['id', 26878], ['id', 47297], ['id', 51854], ['id', 17540]], 'labels': [3, 3, 8, 5, 1], 'scores': [0.7995109558105469, 0.6098806262016296, 0.7271486520767212, 0.8295850157737732, 0.8087340593338013]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9800640940666199})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5257241725921631})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4591643512248993})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3947119116783142})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3881155550479889})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36572426557540894})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.38385576009750366})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4080137014389038})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4134514331817627})
store['active_learning_steps'][45]['training']['best_epoch']=6
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9526, 'crossentropy': 0.3439784912109375}
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 52133], ['id', 41594], ['id', 7368], ['id', 22065], ['ood', 3967]], 'labels': [0, 9, 5, 1, 5], 'scores': [0.7015584707260132, 0.5864754915237427, 0.701133131980896, 0.7718559503555298, 0.2764408588409424]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0586206912994385})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5282183885574341})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.43843263387680054})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3689633309841156})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3760461211204529})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.36162060499191284})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.40041810274124146})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.38405364751815796})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3721678853034973})
store['active_learning_steps'][46]['training']['best_epoch']=6
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9508, 'crossentropy': 0.3217668701171875}
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 8458], ['id', 2803], ['id', 8883], ['id', 13432], ['id', 24589]], 'labels': [4, 3, 2, 2, 8], 'scores': [0.814828634262085, 0.6620405316352844, 0.8437405228614807, 0.7092338800430298, 0.8922368288040161]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.1300864219665527})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6177390217781067})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.48809924721717834})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4158245921134949})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.40448522567749023})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3840252757072449})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.43293535709381104})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.40698331594467163})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4050150513648987})
store['active_learning_steps'][47]['training']['best_epoch']=6
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9477, 'crossentropy': 0.3638984130859375}
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 8355], ['id', 44202], ['id', 39208], ['id', 33365], ['id', 24031]], 'labels': [0, 8, 5, 5, 6], 'scores': [0.4888060390949249, 0.7281279563903809, 0.776036262512207, 0.5816603899002075, 0.41150200366973877]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.069564938545227})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6106076240539551})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.41672492027282715})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.42396801710128784})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4156951308250427})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3745938241481781})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3759806752204895})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4278535842895508})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.49353355169296265})
store['active_learning_steps'][48]['training']['best_epoch']=6
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9454, 'crossentropy': 0.3731401611328125}
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 53927], ['ood', 47952], ['id', 54701], ['id', 5630], ['id', 25748]], 'labels': [7, 0, 8, 1, 7], 'scores': [0.695719838142395, 0.4746272563934326, 0.519645094871521, 0.7027133703231812, 0.7391530871391296]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.0613605976104736})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5309690237045288})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.45191100239753723})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.411723256111145})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.40323537588119507})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3611795902252197})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.38304975628852844})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3828568160533905})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.41877976059913635})
store['active_learning_steps'][49]['training']['best_epoch']=6
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9522, 'crossentropy': 0.3361208251953125}
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 52674], ['ood', 9030], ['id', 27292], ['id', 23350], ['id', 42838]], 'labels': [6, 5, 7, 8, 9], 'scores': [0.7272436618804932, 0.421614408493042, 0.8887841701507568, 0.7506246566772461, 0.748793363571167]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.0081197023391724})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5479928255081177})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4234488308429718})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.35675665736198425})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.376228392124176})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.34847187995910645})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.381348192691803})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.36100468039512634})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33548232913017273})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33871644735336304})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3960036039352417})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.37520331144332886})
store['active_learning_steps'][50]['training']['best_epoch']=9
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9569, 'crossentropy': 0.3122184814453125}
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 14984], ['id', 42703], ['id', 29189], ['id', 7920], ['id', 14385]], 'labels': [9, 0, 8, 2, 8], 'scores': [0.6443896293640137, 0.6115144491195679, 0.6146430969238281, 0.6656161546707153, 0.6561738848686218]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9978852272033691})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5395781993865967})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4159967005252838})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3426128625869751})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.347654789686203})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3734007477760315})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3128640949726105})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3392285108566284})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32212328910827637})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32734084129333496})
store['active_learning_steps'][51]['training']['best_epoch']=7
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9578, 'crossentropy': 0.3131903564453125}
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 9096], ['id', 43042], ['id', 42059], ['id', 45446], ['id', 9392]], 'labels': [5, 8, 9, 7, 4], 'scores': [0.71603724360466, 0.7358726859092712, 0.6226173341274261, 0.8000519275665283, 0.737587034702301]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9926283955574036})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5441937446594238})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.40065380930900574})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4291858673095703})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3522225320339203})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36108893156051636})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36981871724128723})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.35969433188438416})
store['active_learning_steps'][52]['training']['best_epoch']=5
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.952, 'crossentropy': 0.3377324462890625}
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 15538], ['id', 8117], ['id', 8104], ['id', 1134], ['id', 2477]], 'labels': [5, 4, 5, 2, 7], 'scores': [0.6597074866294861, 0.7800308465957642, 0.5986623764038086, 0.5815838575363159, 0.524273544549942]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.1489834785461426})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.589556097984314})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.43749678134918213})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3773634135723114})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3617496192455292})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3548443913459778})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3376595973968506})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3112511932849884})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33992958068847656})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35529041290283203})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3467193841934204})
store['active_learning_steps'][53]['training']['best_epoch']=8
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9624, 'crossentropy': 0.2893042236328125}
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 23260], ['id', 18090], ['id', 30688], ['id', 56457], ['id', 44570]], 'labels': [7, 5, 8, 3, 7], 'scores': [0.6183032989501953, 0.5558346509933472, 0.7357075214385986, 0.7881626486778259, 0.7512726187705994]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0607318878173828})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5296022891998291})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.42584532499313354})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3585429787635803})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33684229850769043})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30877184867858887})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3273389935493469})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32434219121932983})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3287569284439087})
store['active_learning_steps'][54]['training']['best_epoch']=6
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9601, 'crossentropy': 0.2868466064453125}
store['active_learning_steps'][54]['acquisition']={'indices': [['id', 35128], ['id', 36818], ['id', 38510], ['id', 21495], ['id', 41929]], 'labels': [2, 7, 8, 9, 3], 'scores': [0.5392259955406189, 0.8134370446205139, 0.5468057990074158, 0.609382152557373, 0.5531672835350037]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.0519715547561646})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5419448614120483})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3991629481315613})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3501322269439697})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3303927183151245})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3329662084579468})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.333010196685791})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3311241865158081})
store['active_learning_steps'][55]['training']['best_epoch']=5
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9586, 'crossentropy': 0.31900078125}
store['active_learning_steps'][55]['acquisition']={'indices': [['id', 37469], ['id', 45666], ['id', 42673], ['id', 36132], ['id', 8110]], 'labels': [2, 1, 1, 3, 0], 'scores': [0.8476881980895996, 0.7906705141067505, 0.7658040523529053, 0.5802766382694244, 0.5068861246109009]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.0960276126861572})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.605527400970459})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4391321837902069})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33884310722351074})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3678450882434845})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35120850801467896})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3483789563179016})
store['active_learning_steps'][56]['training']['best_epoch']=4
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9581, 'crossentropy': 0.3318682373046875}
store['active_learning_steps'][56]['acquisition']={'indices': [['id', 8552], ['id', 1740], ['id', 52358], ['id', 33752], ['id', 2759]], 'labels': [2, 9, 2, 1, 7], 'scores': [0.7093522548675537, 0.6225125789642334, 0.7720805406570435, 0.5597382187843323, 0.42167866230010986]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.0078248977661133})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5228763222694397})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37010008096694946})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3351665139198303})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32415348291397095})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28556615114212036})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30740904808044434})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28514599800109863})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32309865951538086})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31648415327072144})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.34294041991233826})
store['active_learning_steps'][57]['training']['best_epoch']=8
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9659, 'crossentropy': 0.2680276611328125}
store['active_learning_steps'][57]['acquisition']={'indices': [['id', 55015], ['id', 44131], ['id', 4822], ['id', 27083], ['id', 14286]], 'labels': [8, 1, 4, 7, 3], 'scores': [0.733249306678772, 0.591442883014679, 0.6034642457962036, 0.6567410826683044, 0.9165797531604767]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.2991591691970825})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6602543592453003})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.41441023349761963})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3741941452026367})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3337544798851013})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3537372350692749})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3527868986129761})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31663209199905396})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3202136754989624})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.36378800868988037})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3710174560546875})
store['active_learning_steps'][58]['training']['best_epoch']=8
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9631, 'crossentropy': 0.292300390625}
store['active_learning_steps'][58]['acquisition']={'indices': [['id', 10744], ['id', 58422], ['id', 138], ['id', 50417], ['id', 25350]], 'labels': [7, 9, 5, 3, 7], 'scores': [0.8767432570457458, 0.6407922506332397, 0.6747152805328369, 0.7955981492996216, 0.4550768733024597]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.128848671913147})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.639995813369751})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3959721326828003})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3079018294811249})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34566324949264526})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35389819741249084})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30843040347099304})
store['active_learning_steps'][59]['training']['best_epoch']=4
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9639, 'crossentropy': 0.31591474609375}
store['active_learning_steps'][59]['acquisition']={'indices': [['id', 13498], ['id', 16430], ['id', 21968], ['id', 47662], ['id', 50556]], 'labels': [8, 6, 4, 9, 6], 'scores': [0.493560791015625, 0.5909140110015869, 0.5803476572036743, 0.5419410467147827, 0.6525970697402954]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.0883021354675293})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4862440824508667})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.39488348364830017})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33464935421943665})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3244692087173462})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2981562912464142})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3178950250148773})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3290277123451233})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29365575313568115})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30852818489074707})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31115472316741943})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3473256528377533})
store['active_learning_steps'][60]['training']['best_epoch']=9
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9663, 'crossentropy': 0.2566340576171875}
store['active_learning_steps'][60]['acquisition']={'indices': [['id', 13676], ['id', 53872], ['id', 45520], ['id', 41266], ['id', 33162]], 'labels': [3, 8, 8, 1, 8], 'scores': [0.507641613483429, 0.9127614498138428, 0.7335141897201538, 0.5264883041381836, 0.7828188538551331]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.1090891361236572})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5109886527061462})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.37841886281967163})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35044053196907043})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30965542793273926})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2894296646118164})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32156234979629517})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3213196396827698})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3080218434333801})
store['active_learning_steps'][61]['training']['best_epoch']=6
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9673, 'crossentropy': 0.26429365234375}
store['active_learning_steps'][61]['acquisition']={'indices': [['id', 14329], ['id', 26412], ['id', 32047], ['id', 49728], ['id', 50639]], 'labels': [0, 3, 9, 5, 8], 'scores': [0.5811951160430908, 0.6357033848762512, 0.7179279327392578, 0.6867383122444153, 0.6852495074272156]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.1749334335327148})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5627498030662537})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3447444438934326})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32876768708229065})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3171083927154541})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2960306406021118})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30570170283317566})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2938719391822815})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3103804290294647})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30108729004859924})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29598480463027954})
store['active_learning_steps'][62]['training']['best_epoch']=8
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9691, 'crossentropy': 0.268947998046875}
store['active_learning_steps'][62]['acquisition']={'indices': [['id', 7434], ['id', 40977], ['id', 56480], ['id', 17808], ['id', 33581]], 'labels': [6, 9, 9, 8, 9], 'scores': [0.6877875328063965, 0.5353052914142609, 0.6387348771095276, 0.5452310740947723, 0.653632402420044]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.1002020835876465})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5882428884506226})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4248580038547516})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34936267137527466})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33242976665496826})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32023245096206665})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3218705654144287})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30401214957237244})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30009737610816956})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2936423122882843})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3083321452140808})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3341200351715088})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29065990447998047})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3085235357284546})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31668853759765625})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3168056011199951})
store['active_learning_steps'][63]['training']['best_epoch']=13
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9715, 'crossentropy': 0.2542056640625}
store['active_learning_steps'][63]['acquisition']={'indices': [['id', 13149], ['id', 27545], ['id', 56006], ['id', 52169], ['id', 43950]], 'labels': [7, 8, 3, 2, 9], 'scores': [0.9301436543464661, 0.7450793087482452, 0.9029659628868103, 0.9277828335762024, 0.746427595615387]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.084191083908081})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5938667058944702})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.383952260017395})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.37287575006484985})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31509166955947876})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31638094782829285})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30498838424682617})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27923160791397095})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3052796721458435})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2862131595611572})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29261863231658936})
store['active_learning_steps'][64]['training']['best_epoch']=8
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9659, 'crossentropy': 0.25904013671875}
store['active_learning_steps'][64]['acquisition']={'indices': [['id', 55028], ['id', 5129], ['id', 4061], ['id', 24630], ['id', 36421]], 'labels': [3, 2, 7, 5, 3], 'scores': [0.5282390117645264, 0.8458850979804993, 0.42220351099967957, 0.5147438049316406, 0.6726258993148804]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.1374187469482422})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5411966443061829})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3792324662208557})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.37524086236953735})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3042657971382141})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27568840980529785})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2887609601020813})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2621558904647827})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2571462094783783})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26940542459487915})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2851192355155945})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30904412269592285})
store['active_learning_steps'][65]['training']['best_epoch']=9
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9701, 'crossentropy': 0.2473912109375}
store['active_learning_steps'][65]['acquisition']={'indices': [['id', 48880], ['id', 8854], ['id', 20641], ['id', 51337], ['id', 32073]], 'labels': [4, 4, 9, 4, 8], 'scores': [0.7445818781852722, 0.7269459962844849, 0.8710918426513672, 0.8126181960105896, 0.7526134252548218]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0877647399902344})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.579238772392273})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4057551920413971})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3237030804157257})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3077647089958191})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3077329397201538})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2900678217411041})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2983827292919159})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25363588333129883})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2872124910354614})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2446187138557434})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27748793363571167})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2846018671989441})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2923819124698639})
store['active_learning_steps'][66]['training']['best_epoch']=11
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9687, 'crossentropy': 0.2761907470703125}
store['active_learning_steps'][66]['acquisition']={'indices': [['id', 42434], ['id', 47432], ['id', 22199], ['id', 11584], ['id', 58560]], 'labels': [3, 6, 2, 0, 0], 'scores': [0.6347223520278931, 0.8958208560943604, 0.8020025491714478, 0.7529701590538025, 0.8084656596183777]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.224216341972351})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6509139537811279})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4431747794151306})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37709420919418335})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33633658289909363})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33515655994415283})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3175331950187683})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3067362904548645})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3252941966056824})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34759780764579773})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32094472646713257})
store['active_learning_steps'][67]['training']['best_epoch']=8
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9648, 'crossentropy': 0.2768669189453125}
store['active_learning_steps'][67]['acquisition']={'indices': [['id', 37648], ['id', 36731], ['id', 41832], ['id', 8116], ['id', 43310]], 'labels': [4, 1, 2, 0, 9], 'scores': [0.7527689337730408, 0.5388430953025818, 0.5909854173660278, 0.7035201787948608, 0.7901844382286072]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.2265114784240723})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.6023553013801575})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.41783758997917175})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33116233348846436})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2957596778869629})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.309039831161499})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29904112219810486})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2732829451560974})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29311347007751465})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2979240417480469})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3114662766456604})
store['active_learning_steps'][68]['training']['best_epoch']=8
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9698, 'crossentropy': 0.2645882080078125}
store['active_learning_steps'][68]['acquisition']={'indices': [['id', 26150], ['id', 12936], ['id', 39673], ['id', 54586], ['ood', 24945]], 'labels': [5, 8, 2, 9, 9], 'scores': [0.5847142934799194, 0.8294820785522461, 0.7861514687538147, 0.6126912236213684, 0.37295401096343994]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.3079930543899536})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.6205519437789917})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4004138708114624})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31015706062316895})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2958884835243225})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2788514196872711})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2881390452384949})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.26043200492858887})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.27848750352859497})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2756137251853943})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.24337121844291687})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2831743359565735})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26982441544532776})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2835980951786041})
store['active_learning_steps'][69]['training']['best_epoch']=11
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9712, 'crossentropy': 0.2451971923828125}
store['active_learning_steps'][69]['acquisition']={'indices': [['id', 4185], ['id', 53998], ['id', 44534], ['id', 21906], ['id', 29259]], 'labels': [2, 9, 9, 4, 8], 'scores': [0.8635316491127014, 0.6387764513492584, 0.7392840385437012, 0.46228477358818054, 0.511451780796051]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.1057751178741455})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.6171692609786987})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.40831056237220764})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.34787464141845703})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.33928775787353516})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.27924710512161255})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28506115078926086})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28059446811676025})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2816791534423828})
store['active_learning_steps'][70]['training']['best_epoch']=6
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9672, 'crossentropy': 0.2847273193359375}
store['active_learning_steps'][70]['acquisition']={'indices': [['id', 27758], ['id', 10616], ['id', 207], ['id', 42178], ['id', 53758]], 'labels': [7, 2, 3, 3, 3], 'scores': [0.47680699825286865, 0.6885564625263214, 0.8386650085449219, 0.5269497036933899, 0.6343675553798676]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.1648972034454346})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6044606566429138})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.4115901589393616})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.3259314298629761})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.30846720933914185})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27641406655311584})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2711412310600281})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26706355810165405})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2736513912677765})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2686381936073303})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.257459819316864})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2693895995616913})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2712123990058899})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29314160346984863})
store['active_learning_steps'][71]['training']['best_epoch']=11
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9742, 'crossentropy': 0.2363895263671875}
store['active_learning_steps'][71]['acquisition']={'indices': [['id', 57985], ['id', 55758], ['id', 36376], ['id', 51863], ['id', 39378]], 'labels': [4, 3, 0, 9, 8], 'scores': [0.8892505168914795, 0.7003284096717834, 0.7755865454673767, 0.7879108190536499, 0.6641929447650909]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.1687581539154053})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5937684774398804})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.47594568133354187})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3577931523323059})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32406502962112427})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3098425567150116})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28622525930404663})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.28835052251815796})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2826788127422333})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2730254530906677})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2610512971878052})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27099335193634033})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28671687841415405})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2650865912437439})
store['active_learning_steps'][72]['training']['best_epoch']=11
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9683, 'crossentropy': 0.2493629150390625}
store['active_learning_steps'][72]['acquisition']={'indices': [['ood', 31856], ['id', 30968], ['id', 33088], ['id', 43946], ['id', 36286]], 'labels': [9, 6, 2, 5, 4], 'scores': [0.30214357376098633, 0.7252536416053772, 0.47175222635269165, 0.4553396701812744, 0.7133786678314209]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1087311506271362})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.572389543056488})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3833589255809784})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2989480495452881})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30603086948394775})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28783684968948364})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27586662769317627})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29763227701187134})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2624872922897339})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2915616035461426})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.28095442056655884})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29964953660964966})
store['active_learning_steps'][73]['training']['best_epoch']=9
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9736, 'crossentropy': 0.243809814453125}
store['active_learning_steps'][73]['acquisition']={'indices': [['id', 31428], ['id', 45784], ['id', 23912], ['id', 25546], ['id', 31554]], 'labels': [3, 9, 5, 8, 5], 'scores': [0.7428433895111084, 1.0475539565086365, 0.5162318646907806, 0.6456928253173828, 0.8653939962387085]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.174818515777588})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5826449990272522})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.4429146945476532})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.39588603377342224})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3420293629169464})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29278919100761414})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29180434346199036})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.285433292388916})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2792419195175171})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2769472002983093})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2832642197608948})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31462180614471436})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.28347527980804443})
store['active_learning_steps'][74]['training']['best_epoch']=10
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9706, 'crossentropy': 0.2536219970703125}
store['active_learning_steps'][74]['acquisition']={'indices': [['id', 10086], ['id', 53148], ['id', 6291], ['id', 224], ['id', 56162]], 'labels': [7, 6, 3, 1, 6], 'scores': [0.5678537487983704, 0.5813358426094055, 0.6135573387145996, 0.923502504825592, 0.6966567635536194]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.1518689393997192})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5653225779533386})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.47557055950164795})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.315949022769928})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3138524889945984})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27958452701568604})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28262054920196533})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24938583374023438})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2769421637058258})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24886122345924377})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24893712997436523})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26012396812438965})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2610241770744324})
store['active_learning_steps'][75]['training']['best_epoch']=10
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9731, 'crossentropy': 0.2277690185546875}
store['active_learning_steps'][75]['acquisition']={'indices': [['id', 23008], ['id', 57931], ['id', 32072], ['id', 49890], ['id', 33388]], 'labels': [8, 1, 8, 5, 8], 'scores': [0.7004112005233765, 0.6677825450897217, 0.4724090099334717, 0.8122057914733887, 0.6837451457977295]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.2053477764129639})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.6212601661682129})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.41670113801956177})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30950260162353516})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29407164454460144})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2844995856285095})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2575480043888092})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2748737335205078})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2561612129211426})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2701951861381531})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2767002284526825})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2673106789588928})
store['active_learning_steps'][76]['training']['best_epoch']=9
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9724, 'crossentropy': 0.243364453125}
store['active_learning_steps'][76]['acquisition']={'indices': [['id', 16019], ['id', 13376], ['id', 134], ['id', 29002], ['id', 12782]], 'labels': [3, 3, 1, 7, 8], 'scores': [0.7334355711936951, 0.8244172930717468, 0.7071688771247864, 0.9605193138122559, 0.7339520454406738]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.1383233070373535})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.6565972566604614})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.40735480189323425})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.304706335067749})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2804911732673645})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2932600975036621})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.25856533646583557})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2556314468383789})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.978515625, 'crossentropy': 0.233578622341156})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.24477240443229675})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2560437321662903})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.2571622133255005})
store['active_learning_steps'][77]['training']['best_epoch']=9
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9741, 'crossentropy': 0.230187109375}
store['active_learning_steps'][77]['acquisition']={'indices': [['id', 17112], ['id', 54880], ['id', 31917], ['id', 27248], ['id', 8790]], 'labels': [8, 5, 9, 3, 3], 'scores': [0.6606715321540833, 0.8630217015743256, 0.8185429573059082, 0.7168641090393066, 0.5744978785514832]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.3503172397613525})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5893453359603882})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.4095030725002289})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.35458236932754517})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.2862171530723572})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2673444449901581})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.29766222834587097})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2700706124305725})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2572386562824249})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29529571533203125})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.27489086985588074})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2847632169723511})
store['active_learning_steps'][78]['training']['best_epoch']=9
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9708, 'crossentropy': 0.2441061767578125}
store['active_learning_steps'][78]['acquisition']={'indices': [['ood', 39878], ['id', 16488], ['id', 53979], ['id', 54002], ['id', 8449]], 'labels': [7, 9, 8, 5, 0], 'scores': [0.5053318738937378, 0.9172201156616211, 0.8567937016487122, 0.6723624467849731, 0.6482841372489929]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.2134950160980225})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5772658586502075})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.4282006323337555})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3076910078525543})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3044845461845398})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2685563564300537})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9794921875, 'crossentropy': 0.24391531944274902})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2300410270690918})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.23286226391792297})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.23147358000278473})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9794921875, 'crossentropy': 0.2516813576221466})
store['active_learning_steps'][79]['training']['best_epoch']=8
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9757, 'crossentropy': 0.2279240234375}
store['active_learning_steps'][79]['acquisition']={'indices': [['id', 56268], ['id', 9390], ['id', 17478], ['id', 212], ['id', 58349]], 'labels': [4, 9, 4, 7, 7], 'scores': [0.6057754755020142, 0.7679228186607361, 0.8718509078025818, 0.627307653427124, 0.4691588878631592]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.2547527551651})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6150170564651489})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.4106873869895935})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3057326078414917})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29697030782699585})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2742803692817688})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25766488909721375})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29492026567459106})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2786818742752075})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2535803020000458})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.978515625, 'crossentropy': 0.24484992027282715})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.25883978605270386})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2660382390022278})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.2502935528755188})
store['active_learning_steps'][80]['training']['best_epoch']=11
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9735, 'crossentropy': 0.2257080810546875}
store['active_learning_steps'][80]['acquisition']={'indices': [['id', 58832], ['ood', 53188], ['id', 10434], ['id', 12181], ['id', 12343]], 'labels': [3, 5, 5, 5, 4], 'scores': [0.8808327317237854, 0.3798147439956665, 0.4663785696029663, 0.8245197832584381, 0.5413285493850708]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.218685507774353})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.6395552754402161})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.38578200340270996})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31916719675064087})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2919083833694458})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.24908500909805298})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.24869182705879211})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2538453936576843})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.24136504530906677})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.978515625, 'crossentropy': 0.254031240940094})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9794921875, 'crossentropy': 0.23123759031295776})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.23768404126167297})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.978515625, 'crossentropy': 0.24326157569885254})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2762411832809448})
store['active_learning_steps'][81]['training']['best_epoch']=11
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9743, 'crossentropy': 0.2316423095703125}
store['active_learning_steps'][81]['acquisition']={'indices': [['id', 19089], ['id', 9591], ['id', 424], ['id', 16981], ['id', 15893]], 'labels': [5, 8, 9, 9, 5], 'scores': [0.9195232391357422, 0.6249780654907227, 0.8927615284919739, 0.799019455909729, 0.4791586399078369]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.117866039276123})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6248339414596558})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.40371233224868774})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3172709047794342})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.27899986505508423})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2566683292388916})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25971829891204834})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.23620080947875977})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.23727485537528992})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26377683877944946})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.24189898371696472})
store['active_learning_steps'][82]['training']['best_epoch']=8
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9719, 'crossentropy': 0.235225}
store['active_learning_steps'][82]['acquisition']={'indices': [['id', 35482], ['id', 40654], ['id', 39746], ['id', 18501], ['id', 22169]], 'labels': [4, 5, 0, 4, 2], 'scores': [0.6531585454940796, 0.835207998752594, 0.4630610942840576, 0.6643511652946472, 0.632587730884552]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.1225553750991821})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.6081987619400024})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4167898893356323})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3304930031299591})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.30799105763435364})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2897588014602661})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2722342014312744})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2836296260356903})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26018038392066956})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31252968311309814})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27593740820884705})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25573068857192993})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2663114070892334})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2794926166534424})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2809563875198364})
store['active_learning_steps'][83]['training']['best_epoch']=12
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9725, 'crossentropy': 0.24345205078125}
store['active_learning_steps'][83]['acquisition']={'indices': [['id', 40158], ['id', 28362], ['id', 56180], ['id', 33505], ['id', 58734]], 'labels': [8, 7, 8, 2, 8], 'scores': [0.5380797982215881, 0.6903088688850403, 0.7177612781524658, 0.9708029627799988, 0.6999787092208862]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.1686418056488037})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6334341764450073})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.4451758563518524})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.34914925694465637})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.32000476121902466})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.25397181510925293})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2936904728412628})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2809968590736389})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.24934719502925873})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.98046875, 'crossentropy': 0.276894211769104})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.269422322511673})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.24532264471054077})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2649020552635193})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.26140838861465454})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.2400457262992859})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.978515625, 'crossentropy': 0.2811025381088257})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.265421062707901})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.27541518211364746})
store['active_learning_steps'][84]['training']['best_epoch']=15
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9739, 'crossentropy': 0.2371923583984375}
store['active_learning_steps'][84]['acquisition']={'indices': [['id', 43194], ['id', 56380], ['id', 2580], ['id', 55128], ['id', 30630]], 'labels': [8, 4, 3, 8, 6], 'scores': [0.7817763686180115, 0.8405060768127441, 0.7932215929031372, 0.9742037653923035, 0.6608175933361053]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.2597726583480835})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6480849385261536})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.42558804154396057})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32886171340942383})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30019158124923706})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.28695937991142273})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2511046528816223})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.22910571098327637})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2707386016845703})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9814453125, 'crossentropy': 0.27284497022628784})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26103997230529785})
store['active_learning_steps'][85]['training']['best_epoch']=8
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9737, 'crossentropy': 0.237381298828125}
store['active_learning_steps'][85]['acquisition']={'indices': [['id', 36744], ['id', 27299], ['id', 14216], ['id', 22501], ['ood', 53990]], 'labels': [1, 8, 9, 9, 5], 'scores': [0.7328005433082581, 0.8126693964004517, 0.3201238512992859, 0.5910199880599976, 0.5702004432678223]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.2628464698791504})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.6698423624038696})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.44256073236465454})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3689430356025696})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3194844722747803})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2917206883430481})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.25656816363334656})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.98046875, 'crossentropy': 0.23711805045604706})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.98046875, 'crossentropy': 0.23646587133407593})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.2280939519405365})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.23998290300369263})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2602074146270752})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9814453125, 'crossentropy': 0.25212201476097107})
store['active_learning_steps'][86]['training']['best_epoch']=10
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9764, 'crossentropy': 0.2271630126953125}
